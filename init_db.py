import psycopg2

def create_table():
    try:
        conn = psycopg2.connect(
            dbname="railway",
            user="postgres",
            password="vVMyqWjrqgVhEnwyFifTQxkDtPjQutGb",
            host="interchange.proxy.rlwy.net",
            port="30451"
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
