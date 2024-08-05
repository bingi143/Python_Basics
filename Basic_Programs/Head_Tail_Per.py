import random
def m1(n):
    if(n<=0):
        return "Enter Positive number"
    Head=0
    Tail=0
    for i in range(1,n):
        v=random.random()
        if(v<0.5):
            Tail=Tail+1
        elif(v<1):
            Head=Head+1
        Heads_Percentage=Head/n*100
        Tails_Percentage=Tail/n*100
        return Heads_Percentage,Tails_Percentage
n=int(input("Enter number:"))
Heads_Percentage,Tails_Percentage=m1(n)
print("Heads Percentage is :",Heads_Percentage)
print("Tails percentage is :",Tails_Percentage)