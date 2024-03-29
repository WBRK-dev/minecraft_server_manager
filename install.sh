#!/bin/bash

if [ ! -f /bin/wget ]; then echo "wget is not installed."; wget; exit; fi
if [ ! -f /bin/screen ]; then echo "screen is not installed."; screen; exit; fi

whoami_user=$(whoami)

if [ ! -d /opt/minecraft/servers ]; then
    echo "Creating minecraft folder."
    sudo mkdir -p /opt/minecraft/servers
    sudo chown -R $whoami_user:$whoami_user /opt/minecraft
fi

echo "Downloading packages."

wget -O /opt/minecraft/main.py https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/main.py > /dev/null 2>&1
sudo wget -O /bin/mcman https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/mcman > /dev/null 2>&1
sudo chmod +x /bin/mcman

echo "Download completed."