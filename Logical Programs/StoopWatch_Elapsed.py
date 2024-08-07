'''@Author: Venkatesh
@Date: 2024-08-02 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Program Aim
Python Program DocString Structure:
"" '''

import time
class StopWatch:
    def __init__(self):
        self.Start = None
        self.Stop = None
    
    def Start_time(self):
        self.Start=time.time()
        print("Stop watch Started ")
    def Stop_time(self):
        self.Stop=time.time()
        elapsed=self.Stop-self.Start
        print("Elapsed time is",elapsed)
stopwatch=StopWatch()
print("Press Enter Button 1 to start")
i=int(input())
if i==1:
    stopwatch.Start_time()
print("Press enter Button 0 to stop")
k=int(input())
if k==0:
    stopwatch.Stop_time()
