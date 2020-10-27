import sqlite3
import os
import json
import time


# Method 1: Read EDDiscovery's SQLite Database:
current_log_id = 0
current_merits = 1650
dbpath = r"C:\Users\AMAN\AppData\Local\EDDiscovery"
project_path = r"F:\WORK\GitHub Projects\PP_Merits_Calc"
os.chdir(dbpath)
conn = sqlite3.connect("EDDUser.sqlite")
if(not conn):
    print("Connection error")
else:
    print("Connection estabilished")
    c = conn.cursor()
    while(True):
        try:
            # Basic listener function
            for data in c.execute("SELECT * FROM JournalEntries ORDER BY Id DESC LIMIT 1;"):        
                if(int(data[0]) != current_log_id):
                    print("An event was found!! Parsing details...")
                    current_log_id = int(data[0])
                    if(int(data[3]) == 100):
                        event_dict = json.loads(data[6])
                        #print(event_dict) <- no need to print now, data comes out fine now
                        #Need to create merit++ and logger function
                        if(event_dict["CrimeType"] == "murder" and event_dict["Bounty"] == 10000):
                            current_merits+=30
                        print("Current Merits:",current_merits)
                    else:
                        print("Event did not match requirements!")
                else:
                    print("Waiting for event... Current Merits :",current_merits)
        except KeyboardInterrupt:
            break 
    print("Closing connection")
    conn.close()
