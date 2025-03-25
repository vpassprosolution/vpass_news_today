import httpx

API_KEY = "k5vJut085d8MiAZM"

def take_screenshot():
    url_to_capture = "https://www.forexfactory.com/calendar"
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
