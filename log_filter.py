import os
import json
from os import curdir
import win32ui


class fileparser():

    logs_path = r"C:\Users\AMAN\Saved Games\Frontier Developments\Elite Dangerous"
    test_path = r"F:\WORK\GitHub Projects\PP_Merits_Calc"
    merits = 0
    count = 0
    def file_open(self,mode):    
        dlg = win32ui.CreateFileDialog(1)
        if(mode == "test"):
            dlg.SetOFNInitialDir(self.test_path)
        else:
            dlg.SetOFNInitialDir(self.logs_path)
        dlg.DoModal()
        self.logfile = dlg.GetPathName()

    def filter_to_file(self):
        with open(self.logfile,"r") as thefile:
            with open("filtered_log_file.log","w+") as outfile:
                try:
                    while(thefile):
                        line = thefile.readline()
                        json_line = json.loads(line)
                        if("event" in json_line["event"]=="CommitCrime"):  <<------ FIX THIS
                            outfile.write(line)
                            if(json_line["Bounty"] == 10000):
                                self.merits+=30
                                self.count+=1
                except: json.decoder.JSONDecodeError:
                    pass

a = fileparser()
a.file_open(mode = "test")
a.filter_to_file()


