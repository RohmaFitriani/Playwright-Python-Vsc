from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://firefox.com")
    print(page.tittle())
    time.sleep(10)
    browser.close()


import asyncio
from playwright.async_api import async_playwright
import time

async def main():
  async with async_playwright() as p:
    browser = await p.firefox.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://firefox.com")
    print(await page.tittle())
    await page.screenshot(path="screenshot.jpeg")
    time.sleep(10)
    await browser.close()
asyncio.run(main())

    

