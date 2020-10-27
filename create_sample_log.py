import random
import time

while(True):
    try:
        with open("randomname.log","a") as file:
            number = random.randint(0,10)
            if(number%2 == 0):
                sample_string = "{\"timestamp\":\"2020-10-25T12:11:29Z\", \"event\":\"CommitCrime\", \"CrimeType\":\"murder\", \"Faction\":\"Felicia Winters\", \"Victim\":\"Federal Agent\", \"Bounty\":10000 }"
                file.writelines(sample_string)
                file.writelines("\n")
            file.close()
    except KeyboardInterrupt:
        print("closing down")
        break