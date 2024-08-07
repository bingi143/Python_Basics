def m1(Year):
    if(Year<=999):
        print("Enter Four Digit number")  #Based on given program want only four digit number
        return
    if(Year%4==0):
        if(Year%100!=0):
            if(Year%400==0):
                print(Year,"is leap year")
            else:
                print(Year,"is a leap year")
        else:
            print(Year,"is not leap year")
    else:
        print(Year,"is not leap year")

Year=int(input("Enter Year:"))
m1(Year)