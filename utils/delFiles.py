# -*- coding: UTF-8 -*-

"""
@Project : Qtech_QRCode
@File    : delFiles.py
@Author  : zhilin.gao
@Date    : 2022/1/10 10:32
"""

import os
import glob


class DelFiles:

    @staticmethod
    def del_files(imgpath: str = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "img")):
        global f
        # imgPath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "img")
        file_count = 0
        if os.path.exists(imgpath):
            try:
                for f in os.listdir(imgpath):
                    del_path = os.path.join(imgpath, f)
                    os.remove(del_path)
                    print("remove file %s." % del_path)
                    file_count = file_count + 1
            except:
                print("删除文件{a}出错！".format(a=f))

            print("共删除文件 {a} 个.".format(a=file_count))

        else:
            os.mkdir(imgpath)
            print("mkdir file %s." % imgpath)

    # @staticmethod
    def del_files_2(self,
                    imgpath: str = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "img")):
        file_count = 0
        filenames = glob.glob(imgpath + r"/*")
        for filename in filenames:
            try:
                os.remove(filename)
                file_count = file_count + 1
                print("remove file %s." % filename)
            except:
                try:
                    os.mkdir(filename)
                    print("mkdir file %s." % filename)
                except:
                    print("del file %s." % filename)
                    self.del_files_2(filename)
        print("共删除文件 {a} 个.".format(a=file_count))

    @staticmethod
    def del_files_with(starwith: str = "", endwith: str = "", containstr: str = "",
                       imgpath: str = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                                   "img")):
        file_count = 0
        listdirs = os.listdir(imgpath)
        if starwith != "":
            if any(listdir.startswith(starwith) for listdir in listdirs):
                for listdir in listdirs:
                    if listdir.startswith(prefix=starwith, start=0):
                        os.remove(os.path.join(imgpath, listdir))
                        file_count = file_count + 1
                        print("remove file %s." % listdir)
                        print("1")
            else:
                print("no file meet the 'startwith' criteria!")

        elif endwith != "":
            if any(listdir.endswith(endwith) for listdir in listdirs):
                for listdir in listdirs:
                    if listdir.endswith(endwith):
                        os.remove(os.path.join(imgpath, listdir))
                        file_count = file_count + 1
                        print("remove file %s." % listdir)
                        print("2")
            else:
                print("no file meet the 'endwith' criteria!")

        elif containstr != "":
            if any(containstr in listdir for listdir in listdirs):
                for listdir in listdirs:
                    if containstr in listdir:
                        os.remove(os.path.join(imgpath, listdir))
                        file_count = file_count + 1
                        print("remove file %s." % listdir)
                        print("3")
            else:
                print("no file meet the 'contain' criteria!")

        print("共删除文件 %s 个." % file_count)


if __name__ == '__main__':
    delFiles = DelFiles()
    # delFiles.del_files()
    # delFiles.del_files_2()
    delFiles.del_files_with(endwith="png")
