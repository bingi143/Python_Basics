'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
from datetime import date

def days_between(_date1,_date2):
    d1=date(*_date1)
    d2=date(*_date2)
    date_result=d2-d1
    return date_result.days

_date1=2014,7,2
_date2=2014,7,21

between_days=days_between(_date1,_date2)
print(between_days.days)
