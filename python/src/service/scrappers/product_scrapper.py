import asyncio
from playwright.async_api import async_playwright
import psycopg2
import os
from dotenv import load_dotenv
from src.service.dto.category_products import CategoryProducts
from src.model.category import Category
from src.repository.category_repository import category_repository
from src.service.parser.product_parser_facade import product_parser
from src.service.dto.scrapping.raw_product import RawProduct

load_dotenv()


class ProductScrapper():
    def __init__(self):
        self.url = os.getenv("BREEZY_URL") + "category"

    async def extract_products(self):
        async with async_playwright() as playwright:
            categories = category_repository.fetch_all()

            browser = await playwright.chromium.launch(headless=True)
            page = await browser.new_page()
            category_products = []
            for category in categories:
                print(category)
                product_headlines = []

                full_url = self.url + "/" + category.name
                page_number = 1
                while True:
                    await page.goto(full_url + f"?page={page_number}")
                    if not await self.page_has_results(page):
                        break
                    product_headlines.extend(await self.scrape_products(page))
                    page_number += 1

                products = []
                for product_headline in product_headlines:
                    try:
                        product = product_parser.parse(product_headline)
                    except Exception as e:
                        print("Error: ", e)
                        print("Problem", product_headline)
                        product = None
                    if product is None:
                        continue

                    products.append(product)
                category_products.append(CategoryProducts(category.id, products))

        return category_products

    async def scrape_products(self, page) -> list[RawProduct]:
        index = 1
        raw_products = []
        while True:
            product_headline_xpath = f'//*[@id="__nuxt"]/div/div/div[1]/main/div/div/section/div/div[2]/div/div[2]/div[2]/ul/li[{index}]/div/div[2]/a/h2'
            price_xpath = f'//*[@id="__nuxt"]/div/div/div[1]/main/div/div/section/div/div[2]/div/div[2]/div[2]/ul/li[{index}]/div/div[3]/div/div[1]/div/div/div[2]/div/div/span/div/div/span[1]'
            try:
                product_element = await page.query_selector(product_headline_xpath)
                if not product_element:
                    break

                price_element = await page.query_selector(price_xpath)
                if not price_element:
                    break

                product_headline = await product_element.text_content()
                product_price = await price_element.text_content()

                raw_product = RawProduct(product_headline, product_price)
                raw_products.append(raw_product)

                index += 1
                print("Found product: ", raw_product)
            except Exception as e:
                print("Error:", e)
                break
        return raw_products

    async def page_has_results(self, page):
        product_xpath = f'//*[@id="__nuxt"]/div/div/div[1]/main/div/div/section/div/div[2]/div/div[2]/div[2]/ul/li[1]'
        product_element = await page.query_selector(product_xpath)
        if not product_element:
            return False
        return True


product_scrapper = ProductScrapper()
