import asyncio

from src.service.scrappers.category_scrapper import category_scrapper
from src.service.modifier.category_modifier import category_modifier

class CategoryScrapeManager():
    def scrape(self):
        categories = asyncio.run(category_scrapper.extractCategories())
        category_modifier.create(categories)

category_scrape_manager = CategoryScrapeManager()