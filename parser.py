from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime

def get_today_news_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.forexfactory.com/calendar", timeout=60000)
        page.wait_for_timeout(4000)  # wait for content to fully load

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    today_str = datetime.utcnow().strftime("%b %d")  # Example: 'Mar 25'
    today_header = f"📅 HIGH-IMPACT NEWS – {datetime.utcnow().strftime('%A, %B %d')}\n\n"

    news_items = []
    rows = soup.select("tr.calendar__row")

    for row in rows:
        date_cell = row.select_one(".calendar__date")
        time_cell = row.select_one(".calendar__time")
        currency = row.select_one(".calendar__currency")
        impact = row.select_one(".calendar__impact span")
        title = row.select_one(".calendar__event-title")

        if not (date_cell and impact and currency and title):
            continue

        date_text = date_cell.get_text(strip=True)
        if today_str not in date_text:
            continue

        # Only red folder (high impact)
        impact_class = impact.get("class", [])
        if not any("high" in cls.lower() for cls in impact_class):
            continue

        # Format
        news_items.append(
            f"⏰ {time_cell.get_text(strip=True)} | {currency.get_text(strip=True)} | 🔴 {title.get_text(strip=True)}"
        )

    if not news_items:
        return "Today doesn't have any high-impact news."

    return today_header + "\n".join(news_items)
