'''@Author: Venkatesh
@Date: 2024-08-03 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
import sys
class DayOfWeek:
    @staticmethod
    def day_method(m,d,y):
        y0 = y - (14-m)/12
        x = y0 +y0/4-y0/100+y0/400
        m0 = m +12*((14-m))/12-2
        d0 = (d+x+31*m0/12)% 7

        return d0
if __name__=="__main":

   
   
if __name__=="__main":
     if len(sys.argv)!=4:
        print("use python script.py month day year")
        sys.exit(1)
    month=int(sys.argv[1])
    day=int(sys.argv[2])
    year=int(sys.argv[3])
    
    day_Of_week=DayOfWeek.day_method(month,day,year)
    print(f"day of the week :{day_Of_week}")