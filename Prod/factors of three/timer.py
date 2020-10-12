'''
Author: Lee Brown
Purpose:  This is a simple timer.  It will allow the user to start and stop the timer with two functions.
Explanation:  This module uses the datetime.datetime.now() function to record the time that the timer is started and stopped, subtracting these to obtain the time elapsed.  This output is
returned to the endTimer function.  The only data that is stored within a timer object is the data for the last time that the timer was started and the last endTimer function results.
Notes:
 - Output is not saved.  Any output the developer wishes to save should be saved from the returned startTimer and endTimer object functions within the specific program.
 - For those who are looking to make multiple timer markers from the original start, all that is required is to run the endTimer function again.  This will use the original start time
   and the new end time to create a new return value.

Links and Helpful topics Used:
 - http://net-informations.com/python/iq/self.htm#:~:text=%27self%27%20in%20Python%20The%20self%
 - https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
 - With a little experimentation in the Python command window, I found out that you can subtract the datetime.now() format.
'''
import datetime


class timer:
    def __init__(self):
        self.start = datetime.datetime.now()
        self.end = datetime.datetime.now()
        self.result = self.end - self.start
    def startTimer(self):
        self.start = datetime.datetime.now()
        return self.start
    def endTimer(self):
        self.end = datetime.datetime.now()
        self.result = self.end - self.start
        return self.result

def main():
    newTimer = timer()
    newTimer.startTimer()
    value = input("Press enter to stop the timer.")
    print("h:mm:ss.sssss | " + str(newTimer.endTimer()))
