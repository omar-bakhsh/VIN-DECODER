import cv2
import pytesseract

# تأكد من أن مسار Tesseract مضبوط (على ويندوز، غير المسار حسب التثبيت)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# جرب صورة واضحة لرقم الهيكل
img = cv2.imread("vin_image.jpg")
if img is None:
    print("Error: Could not load image!")
else:
    text = pytesseract.image_to_string(img)
    print("VIN:", text.strip())