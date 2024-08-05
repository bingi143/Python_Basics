'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
class Square:
    @staticmethod
    def Newton_method(Number):
        if Number<0:
            raise ValueError("not possible with negative number")
        t=Number
        epsilon=1e-15
        while abs(t-Number/t)>epsilon*t:
            t=(Number/t+t)/2.0
        return t
    
def main():
    Number=int(input("Enter Number:"))
    result=Square.Newton_method(Number)
    print(result)
main()