#!/bin/bash

if [ ! -f /bin/wget ]; then echo "wget is not installed."; exit; fi


if [ ! -d /opt/minecraft/servers ]; then
    echo "Creating minecraft folder."
    mkdir -p /opt/minecraft/servers
fi

echo "Downloading packages."

sudo wget -O /opt/minecraft/main.py https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/main.py
sudo wget -O /bin/mcman https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/mcman
sudo chmod +x /bin/mcman

echo "Download completed."