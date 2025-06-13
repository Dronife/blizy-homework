import asyncio

from src.service.scrappers.category_scrapper import category_scrapper
from src.service.synchronizer.brand_synchronizer import brand_synchronizer
from src.service.synchronizer.category_synchronizer import category_synchronizer

class FundamentalsScrapeManager():
    def scrape(self):
        category_names = asyncio.run(category_scrapper.extractCategories())

        brand_synchronizer.sync(category_names)
        category_synchronizer.sync(category_names)

fundamentals_scrape_manager = FundamentalsScrapeManager()