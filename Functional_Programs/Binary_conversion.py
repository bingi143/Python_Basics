'''@Author: Venkatesh
@Date: 2024-08-05 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
class Binary:
    @staticmethod
    def binary_conversion(Number):
        if Number<0:
            raise ValueError("Enter Positive number")
        Resutlt=bin(Number)[2:]
        Final_result=Resutlt.zfill(32) #padding is 4 bytes=32bits
        return Final_result
def main():
    Number=int(input("Enter number:"))
    result=Binary.binary_conversion(Number)
    print(result)
main()
    