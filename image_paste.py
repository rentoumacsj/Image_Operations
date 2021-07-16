from PIL import Image
from PIL import Image, ImageDraw, ImageFont

# # 定义文字
# text = 'hello word'
# # 引入PIL库中的模块
# draw = ImageDraw.Draw(image)
# # 引入字体样式(第一个参数为字体样式，具体的可以在自己电脑中C:\Windows\Fonts下找；第二个参数为字体的大小)
# font = ImageFont.truetype(r'‪C:\Windows\Fonts\simhei.ttf', 10)
# # 放置到指定位置(第一个100，代表距离图片左边距；第二个100代表距离图片顶部距离；text是定义的文字；fill设置字体颜色值;font是字体引入和大小的变量名称)
# draw.text((100, 100), text, fill='#666', font=font)

bg_name = 'bg_image/bg.jpg'
fg_name = 'sample_output/fg_transparent.png'

fg = Image.open(fg_name)
fg_width = fg.width  # 2448
fg_height = fg.height  # 3061
fg = fg.resize((int(fg_width * 2 / 3), int(fg_height * 2 / 3)))
r, g, b, a = fg.split()

bg = Image.open(bg_name).resize((fg_width, fg_height))
bg_width = bg.width  # 3024
bg_height = bg.height  # 4032

bg.paste(fg, (int(fg_width / 6), int(fg_height / 3)), mask=a)
bg.save("paste_output/sample.png")
