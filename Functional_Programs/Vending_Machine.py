'''@Author: Venkatesh
@Date: 2024-08-03 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''
def find_notes(notes,Change):
    if(Change==0):
        return 0,[]
    All_Combination=[]
    min_notes=float('inf')
    for note in notes:
        if note<=Change:
            number_notes,combination=find_notes(notes,Change-note)
            number_notes +=1
            if number_notes<min_notes:
                min_notes=number_notes
                All_combination=[note]+combination
    return min_notes,All_combination
def Vending_machine(Change):
    notes=[1000,500,100,50,10,5,2,1]
    min_notes,combination_notes = find_notes(notes,Change)
    return min_notes,combination_notes
Change=int(input("Enter change in Rs to return by the vending machine:"))
min_notes,combination_notes=Vending_machine(Change)
print(f"minimum notes :{min_notes}")
print(f"Notes are return :{combination_notes}")