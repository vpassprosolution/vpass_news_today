import psycopg2
import os

def create_table():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_news (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                image BYTEA,
                news_text TEXT
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Table 'daily_news' created or already exists.")

    except Exception as e:
        print("❌ Error creating table:", e)

if __name__ == "__main__":
    create_table()
