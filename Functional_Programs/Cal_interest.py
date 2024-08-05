'''@Author: Venkatesh
@Date: 2024-08-03 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
class Payment:
    @staticmethod
    def monthly_payment(principal,years,rate):
        months=12*years
        interest=rate//(12*100)
        p=principal*interest//1-(1+interest)^(-months)
        return p
    
def main():
    principal = int(input("Enter amount:"))
    years = int(input("Enter years:"))
    rate_of_interest=int(input("Enter interast rate:"))
    #payments=Payment()
    print(Payment.monthly_payment(principal,years,rate_of_interest))
main()