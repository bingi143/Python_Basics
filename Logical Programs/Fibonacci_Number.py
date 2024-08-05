'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def Fibonaci_method(Number):
    a=0
    print(a)
    b=1
    print(b)
    for i in range(2,Number):
        c=a+b
        print(c,end=",")
        a=b
        b=c
def main():
    Number=int(input("Enter How many Fibonacci Series :"))
    Fibonaci_method(Number)
main()