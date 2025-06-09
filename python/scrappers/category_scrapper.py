import asyncio
from playwright.async_api import async_playwright
import psycopg2

DB_CONFIG = {
    'host': 'db',        # or 'localhost' if local
    'database': 'your_db',
    'user': 'your_user',
    'password': 'your_pass'
}

CATEGORY_URL = "https://breezy.pl/en/category/2nd-life-smartphones"

async def scrape_categories():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(CATEGORY_URL)

        # Adjust selector based on actual DOM
        category_elements = await page.query_selector_all("ul.sidebar-categories a")

        categories = []
        for el in category_elements:
            name = await el.inner_text()
            url = await el.get_attribute("href")
            if name and url:
                categories.append((name.strip(), url.strip()))

        await browser.close()
        return categories

def insert_categories(categories):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    for name, url in categories:
        cursor.execute("""
            INSERT INTO categories (name, url)
            VALUES (%s, %s)
            ON CONFLICT (url) DO NOTHING;
        """, (name, url))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    categories = asyncio.run(scrape_categories())
    print(f"Found {len(categories)} categories")
    insert_categories(categories)
