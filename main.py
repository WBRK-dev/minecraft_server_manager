import os, sys, json, subprocess, time

try:
    import requests
except:
    print("The module 'requests' is not installed."); sys.exit()




def update_check():
    if config("dont_check_for_updates", ""): return
    try:
        response = requests.get("https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/version.json")
        response.raise_for_status()

        version = json.loads(response.content)
        if version["version"] > 1:
            print("\nVersion {} available! Use:\n mcman update".format(version["version"]))
    except:
        print("Error while checking for updates.")



# Server handler
def errorMessage(message, command_list):
    print(message)
    if command_list: print(" list ( online )\n start [ server_name ]\n stop [ server_name ]\n attach [ server_name ]\n install [ path_to_server_installer ] [ server_name ]\n remove [ server_name ]\n update\n repair")

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

def install():
    # if os.path.isdir("{}/{}".format(config("minecraft_servers_dir", ""), sys.argv[3])): print("This server already exist."); return
    standalone_install_file = sys.argv[2].split("/")[len(sys.argv[2].split("/")) - 1]
    install_file_path = mc_path + "/" + sys.argv[3] + "/" + standalone_install_file
    server_folder_path = mc_path + "/" + sys.argv[3]

    install_method = 0
    print("Checking for installation method.")
    if "forge" in standalone_install_file: print("Found forge install method."); install_method = "forge"
    else: 
        print("Did not find a usable install method.\n\n1. Forge\n2. Vanilla\nSelect install method by number.")
        install_method = int(input("> "))
        if install_method == 1: install_method = "forge"
        elif install_method == 2: install_method = "vanilla"
    
    print("Creating server folder.")
    os.system("mkdir {}".format(server_folder_path))
    
    print("Copying installation file.")
    os.system("cp {} {}".format(sys.argv[2], server_folder_path))
    
    print(""); os.system("update-java-alternatives -l")
    print("Select java version to use to install the server. Insert one of the paths below.")
    java_path = input("> ")
    if java_path != "": os.system("sudo update-java-alternatives --set "+java_path)
    
    server_file = ""
    print("Starting server installation.")
    if install_method == "forge":
        install_exit_code = os.system("java -jar {} -installServer {}".format(sys.argv[2], server_folder_path))
        print(install_exit_code)
        print("Removing install file.")
        os.system("rm {}".format(install_file_path))
        os.system("rm {}.log".format(standalone_install_file))
        
        print("Starting server.")
        server_file = subprocess.check_output("ls {} | grep forge | head -n 1".format(server_folder_path), shell=True).split(b"\n")[0].decode("utf-8")
        if server_file == "": server_file = subprocess.check_output("ls {} | grep .jar | head -n 1".format(server_folder_path), shell=True).split(b"\n")[0].decode("utf-8")
        if server_file == "": print("Could not find a jar file. Please manually put the filename below."); server_file = input("> ")
        server_install_process = subprocess.Popen("cd {} && java -jar -Xms1024M -Xmx2048M {} nogui".format(server_folder_path, server_file), shell=True); checking = True
        while checking:
            if not server_install_process.poll() is None:
                checking = False
            time.sleep(1)
    else:
        server_install_process = subprocess.Popen("cd {} && java -jar -Xms1024M -Xmx2048M {} nogui --initSettings".format(server_folder_path, standalone_install_file), shell=True); checking = True
        while checking:
            if not server_install_process.poll() is None:
                checking = False
    
    print("Accepting EULA.")
    with open("{}/eula.txt".format(server_folder_path), "w") as eula:
        eula.write("eula=true")

    print("Creating start.sh file.")
    with open("{}/start.sh".format(server_folder_path), "w") as start_sh:
        server_jar_file = ""
        if server_file != "": server_jar_file = server_file
        else: server_jar_file = standalone_install_file
        if java_path != "": start_sh.write('sudo update-java-alternatives --set {}\nscreen -dmS {} bash -c "cd {} && java -jar -Xms1024M -Xmx2048M {} nogui"'.format(java_path, sys.argv[3], server_folder_path, server_jar_file))
        else: start_sh.write('screen -dmS {} bash -c "cd {} && java -jar -Xms1024M -Xmx2048M {} nogui"'.format(sys.argv[3], server_folder_path, server_jar_file))
        
    print("Done. To start server, use:\n mcman start {}".format(sys.argv[3]))

def remove():
    if not os.path.isdir("{}/{}".format(config("minecraft_servers_dir", ""), sys.argv[2])): print("This server does not exist."); return
    print("Removing server folder.")
    os.system("rm -rf {}/{}".format(config("minecraft_servers_dir", ""), sys.argv[2]))

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
    elif sys.argv[1] == "install" and len(sys.argv) == 4:
            install()
    elif sys.argv[1] == "remove" and len(sys.argv) == 3:
            remove()
    else:
        errorMessage("Invalid argument given.", True)
else:
    errorMessage("No argument given.", True)

update_check()