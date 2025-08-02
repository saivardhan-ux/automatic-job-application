import requests

def solve_captcha(api_key, image_path):
    with open(image_path, 'rb') as img:
        response = requests.post(
            "http://2captcha.com/in.php",
            files={"file": img},
            data={"key": api_key, "method": "post"}
        )

    print("🔵 2Captcha response:", response.text)

    # Check if response is OK
    if "OK|" in response.text:
        captcha_id = response.text.split('|')[1]
    else:
        print("❌ ERROR from 2Captcha:", response.text)
        return None

    print("🕒 Waiting for result...")
    while True:
        res = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}")
        if "OK|" in res.text:
            return res.text.split('|')[1]
        elif "CAPCHA_NOT_READY" in res.text:
            continue
        else:
            print("❌ Final error:", res.text)
            return None

# 👇👇👇 REPLACE THIS WITH YOUR REAL API KEY 👇👇👇
api_key = "713f7313f25b7d031cf82fc0156a9a78"
image_path = "captcha_image.jpg"

token = solve_captcha(api_key, image_path)
print("✅ CAPTCHA Text:", token)
