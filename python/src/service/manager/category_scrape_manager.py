import asyncio

from src.service.scrappers.category_scrapper import category_scrapper
from src.service.modifier.category_modifier import category_modifier
from src.service.modifier.brand_modifier import brand_modifier

class CategoryScrapeManager():
    def scrape(self):
        category_names = asyncio.run(category_scrapper.extractCategories())

        brand_modifier.create(category_names)
        category_modifier.create(category_names)

category_scrape_manager = CategoryScrapeManager()