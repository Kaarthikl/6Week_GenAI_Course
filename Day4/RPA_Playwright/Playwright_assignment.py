# Movie Scrapper
import bs4
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import random


def human_delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))


with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    # Create browser context
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    try:

        # Open Bing
        page.goto("https://www.bing.com")

        # Wait until page is fully loaded
        page.wait_for_load_state("domcontentloaded")

        time.sleep(3)

        # Wait for search input
        page.wait_for_selector('textarea[name="q"], input[name="q"]')

        # Locate search box
        search_box = page.locator('textarea[name="q"], input[name="q"]').first

        # Click the search box
        search_box.click()

        time.sleep(2)

        # Clear existing text if any
        search_box.fill("")

        # Enter search query
        search_box.type(
            "luxury swiss watch brands",
            delay=150
        )

        time.sleep(2)

        # Press Enter
        search_box.press("Enter")
        # Wait for results
        page.wait_for_load_state("networkidle")

        human_delay(3, 5)

        # Wait for visible results
        page.wait_for_selector('li.b_algo h2 a', timeout=20000)

        # Locate visible search results
        results = page.locator('li.b_algo h2 a')

        # Count results
        count = results.count()

        print(f"Results found: {count}")

        # Get first visible result
        first_result = results.nth(0)

        # Extract URL
        first_url = first_result.get_attribute("href")

        print("Opening:", first_url)

        # Open directly
        page.goto(first_url)

        # Wait for page load
        page.wait_for_load_state("domcontentloaded")

        page.wait_for_timeout(15000)

        # Get page content
        html_content = page.content()

        # Parse HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # ----------------------------
        # Extract Metadata
        # ----------------------------

        title = soup.title.string if soup.title else "No Title"

        meta_description = ""

        description_tag = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        if description_tag:
            meta_description = description_tag.get("content", "")

        keywords = ""

        keywords_tag = soup.find(
            "meta",
            attrs={"name": "keywords"}
        )

        if keywords_tag:
            keywords = keywords_tag.get("content", "")

        # ----------------------------
        # Extract Visible Text
        # ----------------------------

        page_text = soup.get_text(separator="\n")

        # Clean text
        cleaned_text = "\n".join(
            line.strip()
            for line in page_text.splitlines()
            if line.strip()
        )

        # ----------------------------
        # Save to File
        # ----------------------------

        output_file = "swiss_watch_brands.txt"

        with open(output_file, "w", encoding="utf-8") as file:

            file.write("===== PAGE METADATA =====\n\n")

            file.write(f"Title:\n{title}\n\n")

            file.write(f"URL:\n{page.url}\n\n")

            file.write(f"Description:\n{meta_description}\n\n")

            file.write(f"Keywords:\n{keywords}\n\n")

            file.write("\n\n===== PAGE CONTENT =====\n\n")

            file.write(cleaned_text)

        print(f"\nData saved successfully to: {output_file}")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        browser.close()