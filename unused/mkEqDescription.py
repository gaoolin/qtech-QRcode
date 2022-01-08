# -*- coding: UTF-8 -*-

"""
@Project : Qtech_QRCode
@File    : mkEqDescription.py
@Author  : zhilin.gao
@Date    : 2022/1/8 13:03
"""

# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
#
#
# class MkEqDes:
#
#     def mkeqdes(self, width: int, height: int, qrcode: Image, qrposwidth: int, qrposheight: int):
#
#         fnt = ImageFont.truetype("C:\\WINDOWS\\Fonts\\msyhbd.ttc", 35)
#         # imgNewWidth = 735
#         # imgNewHeight = 270
#         fontLineSpacing = np.trunc(height / 3.375)
#
#         imgNew = Image.new("RGB", width, height, color="white")
#
#         imgNewCopy = imgNew.copy()
#
#         imgNewCopy.paste(qrcode, (qrposwidth, qrposheight))
#
#         ImageDraw.Draw(imgNewCopy)
#
#         imgNewWidthHead = np.trunc(imgNewCopy.width / 15)
#         imgNewHeightHead = np.trunc(imgNewCopy.height / 10)
#
#         imgNewCopy.text((imgNewWidthHead, imgNewHeightHead), u"EQ设备码：{a}".format(a="EQ123456789"), font=fnt,
#                         fill='black')
#         imgNewCopy.text((imgNewWidthHead, imgNewHeightHead + fontLineSpacing), u"机台号：{a}".format(a="GC2AA-0399"),
#                         font=fnt, fill="black")
#         imgNewCopy.text((imgNewWidthHead, imgNewHeightHead + fontLineSpacing * 2), u"线体：{a}".format(a="GC2C-03"),
#                         font=fnt, fill="black")
#
#         return imgNewCopy
