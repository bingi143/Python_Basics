'''@Author: Venkatesh
@Date: 2024-08-05 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def Binary_convertion(Number):
    return bin(Number)
def nibbles(Number):
    return ((Number & 0x0F) << 4) | ((Number & 0xF0) >> 4)
def power(Number):
    p=1
    for i in range(1,Number):
        p=p*2
    return p
def main():
    Number=int(input("Enter Number:"))
    result=Binary_convertion(Number)
    swap_nibbles=nibbles(Number)
    Final_result=Binary_convertion(swap_nibbles)
    print("before swapping niblles",swap_nibbles)
    print("after swappint nubbles",Final_result)
    power_two=power(Number)
    print("Number is power of 2 value is ",power_two)
main()
