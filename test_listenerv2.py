import win32ui
import os
import json
import winsound
import time

logs_path = r"C:\Users\AMAN\Saved Games\Frontier Developments\Elite Dangerous"
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir(logs_path) 
dlg.DoModal()
filename = dlg.GetPathName() 
print(filename)

class DoneException(Exception):
    pass
class SessionOver(DoneException):
    pass

#function to read an infinite number of lines:
def follow(thefile):
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

goal = int(input("Enter Your Personal Goal:"))
print("Opening file:",filename)
logfile = open(filename,"r")
merits = 0
loglines = follow(logfile)
for line in loglines:
    try:
        json_str = json.loads(line)
        if(json_str["event"] == "CommitCrime" and (json_str["Victim"] == "Federal Agent" or json_str["Victim"] == "Federal Courier")):
            merits+=30
            print("Current Session Merits:",merits)
        if(merits>goal):
            raise DoneException
    except DoneException:
        winsound.MessageBeep()
        print("Goal Reached")
    except KeyboardInterrupt:
        print("Quitting")
        break