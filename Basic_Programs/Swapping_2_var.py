def Swap_method(Number_1,Number_2):
    print("Before Swappint Number_1 Value is:",Number_1)
    print("Before swapping Number_2 Value is:",Number_2)
    Number_3=Number_1+Number_2 #We are storing both values in another variable 
    Number_1=Number_3-Number_1
    Number_2=Number_3-Number_1
    print("After Swapping Number_1 Vales:",Number_1)
    print("After Swapping Number-2 value is:",Number_2)
Number_1=int(input("Enter First Number:"))
Number_2=int(input("Enter Second :"))
Swap_method(Number_1,Number_2)