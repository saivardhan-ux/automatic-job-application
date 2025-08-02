from captcha.image import ImageCaptcha

# Create an ImageCaptcha object
image = ImageCaptcha()

# Text you want in the CAPTCHA
captcha_text = "AB12C"

# Generate and save the image
image.write(captcha_text, "captcha_image.jpg")

print("CAPTCHA image saved as captcha_image.jpg")
