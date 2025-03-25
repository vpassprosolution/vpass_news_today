from PIL import Image

def add_watermark():
    base_image_path = "today_news_cropped.png"
    watermark_path = "welcome.png"
    output_path = "today_news_final.png"

    try:
        # Open base and watermark images
        base = Image.open(base_image_path).convert("RGBA")
        watermark = Image.open(watermark_path).convert("RGBA")

        # Resize watermark proportionally (only if too big)
        max_width = 200
        max_height = 100

        wm_width, wm_height = watermark.size
        scale = min(max_width / wm_width, max_height / wm_height)

        if scale < 1:
            new_size = (int(wm_width * scale), int(wm_height * scale))
            watermark = watermark.resize(new_size, Image.Resampling.LANCZOS)

        # Bottom-right position
        base_width, base_height = base.size
        wm_width, wm_height = watermark.size
        padding = 15
        position = (base_width - wm_width - padding, base_height - wm_height - padding)

        # Paste and save
        base.paste(watermark, position, mask=watermark)
        base.save(output_path)

        print("✅ Final image saved as today_news_final.png")

    except Exception as e:
        print("❌ Error adding watermark:", e)

if __name__ == "__main__":
    add_watermark()
