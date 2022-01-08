# -*- coding: UTF-8 -*-

"""
@Project : core
@File    : comm.py
@Author  : zhilin.gao
@Date    : 2022/1/7 16:49
"""

import qrcode
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pandas as pd


class QrCode:

    @staticmethod
    def qr_code(info: str):
        """
        参数 version 表示生成二维码的尺寸大小，取值范围是 1 至 40，最小尺寸 1 会生成 21 * 21 的二维码矩阵，
        version 每增加 1，生成的二维码就会添加 4 个单位大小，例如 version 是 2，则生成 25 * 25 尺寸大小的二维码。

        参数 error_correction 指定二维码的容错系数，分别有以下4个系数：
        ERROR_CORRECT_L: 7%的字码可被容错
        ERROR_CORRECT_M: 15%的字码可被容错
        ERROR_CORRECT_Q: 25%的字码可被容错
        ERROR_CORRECT_H: 30%的字码可被容错

        参数 box_size 表示二维码里每个格子的像素大小。
        参数 border 表示边框的格子宽度是多少（默认是4）
        """
        # 实例化QRCode生成qr对象
        qr = qrcode.QRCode(

            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border=1
        )
        # 调用qrcode的make()方法传入url或者想要展示的内容
        qr.add_data(info)
        # 填充数据
        qr.make(fit=True)
        # 生成图片
        img = qr.make_image()

        # print("qrCode image pixel size: {a}".format(a=img.pixel_size))
        # print("qrCode image width: {a}".format(a=img.width))
        # print("qrCode image height: {a}".format(a=img.height))

        # 保存路径，'.'为当前路径，'..'为当前路径的上一层路径
        img.save("../img/{a}.png".format(a=info))

        return img

    @staticmethod
    def mk_eq_des(info: list, qrcode: Image, qrcodepixel: int, width: int = 735,
                  height: int = 270, ):
        fnt = ImageFont.truetype("C:\\WINDOWS\\Fonts\\msyhbd.ttc", 35)
        # imgNewWidth = 735
        # imgNewHeight = 270
        fontLineSpacing = np.trunc(height / 3.375)

        imgNew = Image.new("RGB", (width, height), color="white")

        imgNewCopy = imgNew.copy()

        imgNewCopy.paste(qrcode, (width - qrcodepixel, height - qrcodepixel))

        # imgNewCopy.show()

        imgDraw = ImageDraw.Draw(imgNewCopy)

        imgNewWidthHead = np.trunc(imgNewCopy.width / 15)
        imgNewHeightHead = np.trunc(imgNewCopy.height / 10)

        # print(imgNewHeightHead)
        # print(imgNewHeightHead)

        imgDraw.text((imgNewWidthHead, imgNewHeightHead), u"EQ设备码：{a}".format(a=info[0]), font=fnt,
                        fill='black')
        imgDraw.text((imgNewWidthHead, imgNewHeightHead + fontLineSpacing), u"机台号：{a}".format(a=info[1]),
                        font=fnt, fill="black")
        imgDraw.text((imgNewWidthHead, imgNewHeightHead + fontLineSpacing * 2), u"线体：{a}".format(a=info[2]),
                        font=fnt, fill="black")

        return imgNewCopy

    @staticmethod
    def get_eq_info(filename: str, path: str = r"../data/"):

        filepath = os.path.join(path, filename)
        df = pd.read_excel(filepath)

        return df


if __name__ == '__main__':
    qrCode = QrCode()
    qr_code = qrCode.qr_code("eq321654987")
    qr_code.show()
