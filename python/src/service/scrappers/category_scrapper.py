import asyncio
from playwright.async_api import async_playwright
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class CategoryScrapper():
    def __init__(self):
        self.url = os.getenv("BREEZY_URL")+"category"
        self.root_categories = [os.getenv("CATEGORY_IPHONES"), os.getenv("CATEGORY_SMARTPHONES")]
        print(self.url)

    async def extractCategories(self):
        categories = []
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            page = await browser.new_page()

            for root_category in self.root_categories:
                full_url = self.url + "/" + root_category
                await page.goto(full_url)

                index = 3
                while True:
                    xpath = f'//*[@id="__nuxt"]/div/div/div[1]/main/div/div/section/div/div[2]/div/div[1]/div/div/div[2]/div[{index}]/a'
                    try:
                        element = await page.query_selector(xpath)
                        if not element:
                            break
                        href = await element.get_attribute("href")
                        if href:
                            parts = href.strip("/").split("/")
                            last_part = parts[-1]
                            categories.append(last_part)
                            print("Found:", last_part)
                        index += 1
                    except Exception as e:
                        print("Error:", e)
                        break

            await browser.close()

        return categories



category_scrapper = CategoryScrapper()