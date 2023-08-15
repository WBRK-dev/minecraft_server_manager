# Minecraft Server Manager
This script has been made to make the management of minecraft servers easier.
### Compatibility
[x] Linux<br>
[ ] Windows<br>
[ ] Mac OS


## How to use
```
mcman list
```
The list command lists all the minecraft servers.
```
mcman list online
```
The list online command lists all the online minecraft servers.
```
mcman start [ server_name ]
```
The start command starts a server.
```
mcman stop [ server_name ]
```
The stop command stops a server.
```
mcman attach [ server_name ]
```
The attach command attaches a cli output from a server.
```
mcman update
```
The update command updates the application.


## Installation
1. Download the script from releases.
2. Allow the script to execute.
3. Execute the script without sudo mode: `./install.sh`

## Install from source
1. Install the packages: `python3` and `screen`.
2. Download the latest main.py from the main branch.
3. Move main.py to a custom location such as '/home/username/apps/mcservermanager/main.py'
4. Create an alias for easier execution. If you're using an ubuntu machine follow the "Creating an alias for easier execution on ubuntu systems." guide below.

### Creating an alias for easier execution on ubuntu systems.
1. Execute this command in a terminal: `nano ~/.bashrc`
2. Go to the bottom of the file.
3. Add this line of code: `alias mcman="python3 /home/your_username/apps/mcservermanager/main.py"`<br>
The path needs to go to your custom location.
4. Save the file.
5. Execute this command in a terminal: `source ~/.bashrc`
