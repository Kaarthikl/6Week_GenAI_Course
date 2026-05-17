from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
import random
import time

app = Flask(__name__)

@app.route('/run-playwright', methods=['GET'])
def run_playwright():

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch_persistent_context(
                user_data_dir="chrome-profile",
                channel="chrome",
                headless=False,
                slow_mo=1000,
                args=[
                    "--disable-blink-features=AutomationControlled"
                ]
            )

            page = browser.new_page()

            # Open Google
            page.goto("https://www.google.com")

            # Random wait
            time.sleep(random.randint(3, 6))

            # Search box
            search_box = page.locator('textarea[name="q"]')

            # Click slowly
            search_box.click()

            time.sleep(2)

            # Type like a human
            search_box.type(
                "latest tamil movies -ai",
                delay=random.randint(150, 300)
            )

            time.sleep(random.randint(2, 4))

            # Press Enter
            page.keyboard.press("Enter")

            # Wait for results
            page.wait_for_load_state("networkidle")

            time.sleep(random.randint(3, 5))

            # Click first result
            first_result = page.locator('a:has(h3)').first

            first_result.click()

            # Wait for page load
            page.wait_for_load_state("domcontentloaded")

            time.sleep(10)

            current_url = page.url

            browser.close()

            return jsonify({
                "status": "success",
                "message": "Playwright automation completed",
                "opened_url": current_url
            })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        })


if __name__ == '__main__':

    app.run(debug=True)