"""
Capture pristine full-color screenshots from the live Next.js app on http://localhost:3000.
"""
import os
import asyncio
from playwright.async_api import async_playwright

FIG_DIR = r"c:\Users\yashv\dev\work in progress\mini project\AiSOC\docs\figures"
os.makedirs(FIG_DIR, exist_ok=True)

async def capture_all_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1600, 'height': 900},
            device_scale_factor=2
        )
        page = await context.new_page()

        # 1. Dashboard (Color)
        await page.goto("http://localhost:3000/dashboard", wait_until="networkidle")
        await asyncio.sleep(2)
        p_dash = os.path.join(FIG_DIR, "app_screenshot_dashboard.png")
        await page.screenshot(path=p_dash)
        print("Captured full-color Dashboard:", p_dash)

        # 2. Alerts Queue & Workbench (Color)
        await page.goto("http://localhost:3000/alerts", wait_until="networkidle")
        await asyncio.sleep(2)
        p_alerts = os.path.join(FIG_DIR, "app_screenshot_alerts.png")
        await page.screenshot(path=p_alerts)
        print("Captured full-color Alerts Queue:", p_alerts)

        # 3. Investigation Workbench (Color for fig6_7)
        p_workbench = os.path.join(FIG_DIR, "fig6_7_workbench_interface.png")
        await page.screenshot(path=p_workbench)
        print("Captured full-color Workbench:", p_workbench)

        # 4. Threat Hunt Surface (Color)
        await page.goto("http://localhost:3000/hunt", wait_until="networkidle")
        await asyncio.sleep(2)
        p_hunt = os.path.join(FIG_DIR, "app_screenshot_hunt.png")
        await page.screenshot(path=p_hunt)
        print("Captured full-color Hunt Console:", p_hunt)

        # 5. Cases Dossier (Color)
        await page.goto("http://localhost:3000/cases", wait_until="networkidle")
        await asyncio.sleep(2)
        p_cases = os.path.join(FIG_DIR, "app_screenshot_cases.png")
        await page.screenshot(path=p_cases)
        print("Captured full-color Cases Console:", p_cases)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_all_screenshots())
