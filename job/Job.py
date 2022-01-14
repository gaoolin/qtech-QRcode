# -*- coding: UTF-8 -*-

"""
@Project : Qtech_QRCode
@File    : job.py
@Author  : zhilin.gao
@Date    : 2022/1/8 9:46
"""

import numpy as np
from core import comm
from PIL import Image
import time

from utils.delFiles import DelFiles

if __name__ == '__main__':

    t0 = time.time()
    i = 0

    delFiles = DelFiles()
    delFiles.del_files_with(endwith="png")

    img = Image.open("../template/template.png")
    imgCopy = img.copy()
    # print(imgCopy.size)

    eqInfoDF = comm.QrCode.get_eq_info("eLableOfEqInfo.xlsx")

    for row in eqInfoDF.iterrows():
        genQrCode = comm.QrCode().qr_code(row[1][1])

        qrSize = genQrCode.pixel_size

        imgNewDes = comm.QrCode().mk_eq_des(row[1], genQrCode, qrSize)

        imgCopy.paste(imgNewDes, (115, 170))

        imgCopy.save("../img/{a}.png".format(a=row[1][1]))

        print("{a}保存完毕。".format(a=row[1][1]))

        i = i + 1

    t1 = time.time()

    print("用时 {a} s".format(a=np.round((t1 - t0), 1)))
    print("制作标签 {a} 个".format(a=i))
