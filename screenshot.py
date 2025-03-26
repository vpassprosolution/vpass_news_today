import httpx
from datetime import datetime, timedelta

API_KEY = "k5vJut085d8MiAZM"

def get_today_and_tomorrow_url():
    today = datetime.utcnow().strftime('%b%d.%Y').lower()
    tomorrow = (datetime.utcnow() + timedelta(days=1)).strftime('%b%d.%Y').lower()
    return f"https://www.forexfactory.com/calendar?range={today}-{tomorrow}"

def take_screenshot():
    # ✅ Clearly screenshots today and tomorrow ONLY.
    url_to_capture = get_today_and_tomorrow_url()
    screenshot_api_url = f"https://api.urlbox.io/v1/{API_KEY}/png"

    params = {
        "url": url_to_capture,
        "full_page": True,
        "width": 1366,
        "height": 768,
        "thumb_width": 1366,
        "format": "png"
    }

    try:
        response = httpx.get(screenshot_api_url, params=params, timeout=60.0)
        response.raise_for_status()

        with open("today_news_raw.png", "wb") as f:
            f.write(response.content)

        print("✅ Screenshot saved as today_news_raw.png")

    except Exception as e:
        print("❌ Error taking screenshot:", e)

if __name__ == "__main__":
    take_screenshot()
