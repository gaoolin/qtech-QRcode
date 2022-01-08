# -*- coding: UTF-8 -*-

"""
@Project : core
@File    : generateImage.py
@Author  : zhilin.gao
@Date    : 2022/1/7 17:01
"""


import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1
)
# 调用qrcode的make()方法传入url或者想要展示的内容
qr.add_data("python前行者公众号")
qr.make(fit=True)  # 填充数据
img = qr.make_image()  # 生成图片
img.show()
img.save("../img/test3.png")