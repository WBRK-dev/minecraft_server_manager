import os, sys, json

try:
    import requests
except:
    print("The module 'requests' is not installed."); exit()

def update_check():
    if config("dont_check_for_updates", ""): return
    try:
        response = requests.get("https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/version.json")
        response.raise_for_status()

        version = json.loads(response.content)
        if version["version"] > 0:
            print("\nVersion {} available! Use:\n mcman update".format(version["version"]))
    except:
        print("Error while checking for updates.")

















# Server handler
def errorMessage(message, command_list):
    print(message)
    if command_list: print(" list ( online )\n start [ server_name ]\n stop [ server_name ]\n attach [ server_name ]")

def config(key, value): 
    if os.path.isfile("config.json"):

        f = open("config.json")
        data = json.load(f)
        if value != "":
            print("No setter yet.")
        else:
            try:
                return data[key]
            except:
                return False
    else:
        return False
    
mc_path = "/opt/minecraft/servers"
if config("minecraft_servers_dir", ""):
    mc_path = config("minecraft_servers_dir", "")

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        if len(sys.argv) == 3 and sys.argv[2] == "online":
            os.system("screen -ls")
        else:
            dirs = os.listdir(mc_path)

            for dir in dirs:
                if os.path.isdir("{}/{}".format(mc_path, dir)):
                    print(dir)
    elif sys.argv[1] == "start":
        if len(sys.argv) == 3 and os.path.isdir("{}/{}".format(mc_path, sys.argv[2])):
            print("Starting {}.".format(sys.argv[2]))
            os.system("sh {}/{}/start.sh".format(mc_path, sys.argv[2]))
        else:
            errorMessage("ERROR: This server does not exist.", True)
    elif sys.argv[1] == "stop":
        if len(sys.argv) == 3 and os.path.isdir("{}/{}".format(mc_path, sys.argv[2])):
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

update_check()