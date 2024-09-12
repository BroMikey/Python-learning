from PIL import Image, ImageDraw, ImageFont

# 打开一张图片
image = Image.open("D:/1_Programming/BasicTools/Python-learning/python_Vision/image.jpg")

# 旋转图片 45 度
rotated_image = image.rotate(45)

# 缩放图片
resized_image = rotated_image.resize((500, 500))

# 添加水印
draw = ImageDraw.Draw(resized_image)
font = ImageFont.load_default()
draw.text((10, 10), "Watermark", font=font, fill=(255, 255, 255))

# 保存处理后的图片
resized_image.save("output_image_with_watermark.jpg")
