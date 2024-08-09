'''@Author: Venkatesh
@Date: 2024-08-05 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
import os
def check_file(file):
    if os.path.isfile(file):
        print("file is exist")
    else:
        print("file not exist")
file="D:\sv\WhatsApp_files\9pVubVHS-08.js.download"

check_file(file)