# -*- coding: UTF-8 -*-

"""
@Project : core
@File    : CompositeImage.py
@Author  : zhilin.gao
@Date    : 2022/1/8 8:35
"""


from PIL import Image
import os
import job.generateQRCode

print(os.getcwd())
img = Image.open("../template/template.png")
imgCopy = img.copy()
print(imgCopy.size)

imgNew = Image.new("RGB", (720, 320), color='white')
# imgNew.show()


# imgCopy.paste(imgNew, (115, 220))

qrCode = job.qr_code('EQ321654987')

qrCode.show()
