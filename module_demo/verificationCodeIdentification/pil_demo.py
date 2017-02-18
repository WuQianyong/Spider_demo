#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

# @Name    : pil_demo
# @Author  : qianyong
# @Time    : 2017-02-10 11:28

from PIL import Image, ImageFilter, ImageColor, ImageFont, ImageDraw
import random


def demo_main():
    # 打开一个jpg 图像
    im = Image.open('test.jpg')

    # 获得画像尺寸
    w, h = im.size
    print('image size is : {} ,{}'.format(w, h))

    # 缩放50%
    # im.thumbnail((w//2,h//2))
    # print('Resize image to: %sx%s' % (w // 2, h // 2))

    # 应用模糊效果
    im2 = im.filter(ImageFilter.BLUR)

    # 查看图片
    im2.show()
    # 保存图像
    # im.save('thumbnail.jpg', 'jpeg')


def rndChar():
    """
    随机字母
    :return:
    """
    return chr(random.randint(65, 90))


def rndColor():
    """
    随机颜色
    :return:
    """
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def creatPic():
    """
    生成验证码图片
    :return:
    """

    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # create a picture obj
    font = ImageFont.truetype(r'C:\Windows\Fonts\consolab.ttf', 36)
    # create a Draw
    draw = ImageDraw.Draw(image)
    # fill each pixel
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # output word
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # vague

    # 模糊:
    image = image.filter(ImageFilter.BLUR)

    image.show()


if __name__ == '__main__':
    # demo_main()

    creatPic()
