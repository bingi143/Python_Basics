'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def Prime_Number(Number):
    c=0
    for i in range(2,(Number//2+1)):
         if Number == 1:
              continue
         if Number%i==0:
             c=c+1
             print("Given number is not prime number")
             break
    if(c==0):
        print("Given number is prime nubmer")
def main():
    Number=int(input("Enter Number:"))
    Prime_Number(Number)
main()