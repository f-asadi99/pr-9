# Edge Detection

from PIL import Image, ImageFilter

image = Image.open(r"Sample.png")
image = image.convert("L")
image = image.filter(ImageFilter.FIND_EDGES)
image.save(r"Edge_Sample.png")
