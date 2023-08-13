import os
import sys

def errorMessage(message, command_list):
    print(message)
    if command_list: print(" list\n start [ server_name ]")

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        if len(sys.argv) == 3 and sys.argv[2] == "online":
            os.system("screen -ls")
        else:
            dirs = os.listdir("/opt/minecraft/servers")

            for dir in dirs:
                if os.path.isdir("/opt/minecraft/servers/"+dir):
                    print(dir)
    elif sys.argv[1] == "start":
        if len(sys.argv) == 3 and os.path.isdir("/opt/minecraft/servers/"+sys.argv[2]):
            print("Starting {}.".format(sys.argv[2]))
            os.system("sh /opt/minecraft/servers/{}/start.sh".format(sys.argv[2]))
        else:
            errorMessage("ERROR: This server does not exist.", True)
    elif sys.argv[1] == "stop":
        if len(sys.argv) == 3 and os.path.isdir("/opt/minecraft/servers/"+sys.argv[2]):
            print("Stopping {}.".format(sys.argv[2]))
            os.system("screen -S {} -X stuff 'stop\n'".format(sys.argv[2]))
        else:
            errorMessage("ERROR: This server does not exist.", True)
    elif sys.argv[1] == "attach" and len(sys.argv) == 3:
            os.system("screen -r "+sys.argv[2])
    else:
        errorMessage("Invalid argument given.", True)
else:
    errorMessage("No argument given.", True)