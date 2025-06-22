from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/126.0.0.0 Safari/537.36")

        context.add_cookies([{
            'name': 'fiverr_session',
            'value': 'a42866af27f27854ca221f0baefdc735',
            'domain': '.fiverr.com',
            'path': '/',
            'httpOnly': True,
            'secure': True,
            'sameSite': 'Lax',
        }])

        page = context.new_page()
        page.goto("https://www.fiverr.com/inbox")
        print(f"🌐 Page title: {page.title()}")

        while True:
            page.reload()
            print(f"✅ Refreshed Fiverr inbox at {time.ctime()}")
            time.sleep(300)

if __name__ == "__main__":
    main()
