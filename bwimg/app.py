from PIL import Image

# add your image here
img = Image.open("image.png")

bnw = img.convert("L")

bnw.save("result_img.png")