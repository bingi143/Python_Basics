'''@Author: Venkatesh
@Date: 2024-08-05 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" ''' 
import os
def list_file(directory):
    print(os.listdir(directory))

def main():
    directory='ML_Basic_Programs'
    list_file(directory)
main()
