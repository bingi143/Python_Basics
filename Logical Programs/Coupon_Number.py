'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
import random
def Generate_Random(Number):
    return random.randint(1,Number)
def Coupon_Number_Method(Number):
    Collect_Coupon=set()
    Attempts=0
    while len(Collect_Coupon)<Number:
        coupon=Generate_Random(Number)
        Collect_Coupon.add(coupon)
        Attempts=Attempts+1
    return Attempts
def main():
    Number=int(input("Enter Number:"))
    print(Coupon_Number_Method(Number))
main()