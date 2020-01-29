from PIL import Image
from pytesseract import image_to_string

print(image_to_string(Image.open('resin/PETE/PETE 3.png'), config ='--psm 6'))