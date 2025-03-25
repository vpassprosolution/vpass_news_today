from PIL import Image

def crop_forexfactory_image():
    input_path = "today_news_raw.png"
    output_path = "today_news_cropped.png"

    try:
        img = Image.open(input_path)

        # 🚀 Final ultra wide + deep crop
        cropped_img = img.crop((220, 0, 1330, 850))  # (left, top, right, bottom)

        cropped_img.save(output_path)
        print("✅ Cropped image saved as today_news_cropped.png")

    except Exception as e:
        print("❌ Error cropping image:", e)

if __name__ == "__main__":
    crop_forexfactory_image()
