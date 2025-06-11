img = open("images.png", "rb")

data = img.read()

cp_img = open("pythonLogo.png", "wb")

cp_img.write(data)

img.close()
cp_img.close()
