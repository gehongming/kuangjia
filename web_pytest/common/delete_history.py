#__author__="G"
#date: 2019/10/29
import os
from common import contants
def remove_files_in_dir(dir):
    files = os.listdir(dir)
    for item in files:
        c_path = os.path.join(dir,item)
        if os.path.isdir(c_path):
            remove_files_in_dir(c_path)
        else:
            os.remove(c_path)

if __name__ == '__main__':
    remove_files_in_dir(contants.screenshot_dir)