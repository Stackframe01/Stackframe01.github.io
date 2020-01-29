from PIL import Image
from PIL import ImageChops

im1 = Image.open("9.png")
im2 = Image.open("9.png")

diff = ImageChops.difference(im2, im1)
print(diff)