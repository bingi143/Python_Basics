def Large_Val_Method(
        Number_1,Number_2,Number_3):
    if(Number_1>Number_2 and Number_1>Number_3):
        print(Number_1," is Big value")
    elif(Number_2>Number_1 and Number_2>Number_3):
        print(Number_2,"is Big Value")
    else:
        print(Number_3," is Big Value")
Number_1=int(input("Enter First Number:"))
Number_2=int(input("Enter secomd Number:"))
Number_3=int(input("Enter First Number:"))
Large_Val_Method(
    Number_1,Number_2,Number_3
)