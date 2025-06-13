import asyncio

from src.service.scrappers.product_scrapper import product_scrapper
from src.service.modifier.product_modifier import product_modifier
from src.service.synchronizer.product_synchronizer import product_synchronizer
from src.service.synchronizer.model_synchorizer import model_synchronizer

class ProductScrapeManager:
    def scrape(self):
        category_products = asyncio.run(product_scrapper.extract_products())
        model_synchronizer.sync_from_products(category_products)
        product_synchronizer.sync(category_products)
        # category_modifier.create(categories)

product_scrape_manager = ProductScrapeManager()