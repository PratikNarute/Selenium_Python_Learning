import datetime

currentDate=datetime.datetime.today().date()
currentTime=datetime.datetime.today().time()
currentDate_Time=datetime.datetime.today()

# Format of date and time
format_currentDate_Time=currentDate_Time.strftime("%y/%m/%d_%H/%M/%S")

print("Current date:", currentDate)
print("currentTime:",currentTime)
print("currentDate_Time:",currentDate_Time)
print("format_currentDate_Time:",format_currentDate_Time)
