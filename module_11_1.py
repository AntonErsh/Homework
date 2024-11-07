from PIL import Image


with Image.open('1566_0.jpg') as image:
    print(image.info)
    im_res = image.resize(size=(400, 300))
    im_res = im_res.rotate(10)
    print(image.getdata())
    im_res = im_res.effect_spread(5)
    im_res.show()
