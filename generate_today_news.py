from screenshot import take_screenshot
from cropper import crop_forexfactory_image
from watermark import add_watermark
from parser import get_today_news_text
from database import save_today_news

def generate_today_news():
    print("🚀 Starting VESSA News Generator...")

    # Step 1: Screenshot
    take_screenshot()

    # Step 2: Crop
    crop_forexfactory_image()

    # Step 3: Add Watermark
    add_watermark()

    # Step 4: Parse today's news text (Investing.com version)
    news_text = get_today_news_text()
    print("📰 Parsed News Text:")
    print(news_text)

    # Step 5: Save image + text to PostgreSQL
    save_today_news("today_news_final.png", news_text)

    print("✅ NEWS GENERATED & SAVED SUCCESSFULLY ✅")

if __name__ == "__main__":
    generate_today_news()
