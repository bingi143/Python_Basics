'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def Perfect_Number_Method(Number):
    sum=0
    #Number_Copy=Number
    for i in range(1,Number):
        if Number%i==0:
            sum=sum+i
    if Number%sum==0:
        print("Given number is Perfect Number")
    else:
        print("Given Number is not a Perfect number")
def main():
    Number=int(input("Enter Number:"))
    Perfect_Number_Method(Number)
main()