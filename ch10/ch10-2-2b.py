from PIL import Image

im = Image.open("koala.jpg")
print(im.size)
im.thumbnail((300, 200))
print(im.size)
im.save("koala_resized03.jpg")
