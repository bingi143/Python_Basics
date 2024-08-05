'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def Reversing_Number_Method(Number):
    Reverse=0
    while Number>0:
        Remainder=Number%10
        Reverse=Reverse*10+Remainder
        Number=Number//10
    print("Reverse of the Number is",Reverse)
def main():
    Number=int(input("Enter Number:"))
    Reversing_Number_Method(Number)
    print("End")
main()
