'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def Prime_Factors(Number):
    for i in range(2,Number):
        if Number%i==0:
            c=True
            for k in range(2,i//2+1):
                if i%k==0:
                    c=False
            if(c):
                print(i)
def main():
    Number=int(input("Enter number:"))
    Prime_Factors(Number)
main()