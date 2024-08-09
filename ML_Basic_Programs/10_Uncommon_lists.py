'''@Author: Venkatesh
@Date: 2024-08-03 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''

color_list_1=set(["white","black","red"])
color_list_2=set(["red","green"])
result=[]
for i in color_list_1:
    if i not in color_list_2:
        result.append(i)
print(result)