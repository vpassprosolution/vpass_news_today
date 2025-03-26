import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # ✅ Clearly load your .env variables locally

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def save_today_news(image_path: str, news_text: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM daily_news")

    with open(image_path, "rb") as f:
        binary_image = f.read()

    cursor.execute(
        "INSERT INTO daily_news (image, news_text) VALUES (%s, %s)",
        (binary_image, news_text)
    )

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Today’s news image + text saved to DB.")

def load_today_news():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT image, news_text FROM daily_news ORDER BY created_at DESC LIMIT 1")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return row[0], row[1]
    return None, None
