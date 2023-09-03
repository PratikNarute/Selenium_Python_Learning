from math import factorial
import datetime
from Python_Learning import Functions


#=====================factorial module==============================
print("Factorial nummber:", factorial(4))

#=====================datetime module==============================
currentDate=datetime.datetime.today().date()
currentTime=datetime.datetime.today().time()
currentDate_Time=datetime.datetime.today()

# Format of date and time
format_currentDate_Time=currentDate_Time.strftime("%y/%m/%d_%H/%M/%S")

print("datetime module-Current date:", currentDate)
print("datetime module-currentTime:",currentTime)
print("datetime module-currentDate_Time:",currentDate_Time)
print("datetime module-format_currentDate_Time:",format_currentDate_Time)

#=====================custom module==============================================
Functions.add(10,10)
Functions.divide(20,10)
