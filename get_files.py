import os, shutil
import logging


s = os.sep
BASE_DIR = os.environ["HOMEPATH"]
FLASH_NAME = r"D:"
FLASH_NAME2 = "44"
if not os.path.exists(FLASH_NAME + s + FLASH_NAME2):
    os.mkdir(FLASH_NAME + s + FLASH_NAME2)


def files_getter(dir_or_file):
    dir_or_file = dir_or_file.replace("\\\\", "\\")
    for files in os.listdir(str(dir_or_file).replace("\\\\", "\\")):
            if os.path.isfile(str(dir_or_file + s + files).replace("\\\\", "\\")):
                shutil.copy(src = str(dir_or_file + s + files).replace("\\\\", "\\"), dst= str(FLASH_NAME  + s + FLASH_NAME2 + s + dir_or_file + s + files).replace("\\\\", "\\"))
            elif os.path.isdir(str(dir_or_file + s + files).replace("\\\\", "\\")):
                if not os.path.exists(str(FLASH_NAME + s +  FLASH_NAME2 + s + files).replace("\\\\","\\")):
                    os.mkdir(str(FLASH_NAME + s + FLASH_NAME2 + s + files).replace("\\\\", "\\"))
                    files_getter(str(dir_or_file + s + files).replace("\\\\", "\\"))
                else:
                    pass
  
  
files_getter(BASE_DIR)

