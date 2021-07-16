from PIL import Image
from PIL import Image, ImageDraw, ImageFont

# 新建一张底色为黑色的图片
image = Image.new('RGB', (1600, 900), "black")

# 打开本地指定的位置的图片
image1 = Image.open("sample_source/fg.jpg").resize((800, 900))
image2 = Image.open("sample_output/fg_black.png").resize((800, 900))
image.paste(image1, (0, 0))
image.paste(image2, (800, 0))
image.save("concat_output/compare.png")
