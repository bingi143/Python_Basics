def Quotient_Remainder_Method(Number_1,Number_2):
    Quotient=Number_1 / Number_2
    Remainder=Number_1 % Number_2
    print(Quotient,"Quotient")
    print(Remainder,"Reminder")
def main():
    Number_1=int(input("Enter number 1 :"))
    Number_2=int(input("Enter Number 2:"))
    Quotient_Remainder_Method(Number_1,Number_2)
main()