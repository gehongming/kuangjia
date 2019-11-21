#__author__="G"
#date: 2019/11/14

from common import contants
import os

def get_filelist(dir):
    Filelist = []

    for home, dirs, files in os.walk(dir):

        for filename in files:

        # 文件名列表，包含完整路径

            Filelist.append(os.path.join(home, filename))

            # 文件名列表，只包含文件名

            # Filelist.append(filename)

    return Filelist

if __name__ == "__main__":

    Filelist = get_filelist(contants.reports_screen)

    print(len(Filelist))

    print(Filelist[-1])
    for file in Filelist:

        print(file)
