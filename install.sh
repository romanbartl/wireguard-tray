#!/bin/bash

FOLDER="/usr/local/bin/wireguard_tray"

is_installed() {
    dpkg -l | grep -qw "$1"
}

echo "Update packages..."
sudo apt update

if is_installed wireguard; then
    echo "WireGuard already installed."
else
    echo "WireGuard not installed. Installing ... "
    sudo apt install -y wireguard
    echo "WireGuard successfuly installed."
fi

echo
echo

echo "Installing Python3 graphical libs"
sudo apt install libappindicator3-dev gir1.2-appindicator3-0.1

echo
echo

echo "Moving WG configuration file"
sudo cp webari.conf /etc/wireguard/webari.conf

echo
echo

echo "Moving conf file for startup"
cp src/wireguard_tray.sh.desktop "/home/$LOGNAME/.config/autostart/wireguard_tray.sh.desktop"

echo
echo

echo "Installing files ..."

if [ -d "$FOLDER" ]; then
    sudo rm -rf "$FOLDER"
else
    echo
fi

sudo mkdir -p "$FOLDER"
sudo mkdir -p "$FOLDER/wireguard"

sudo cp -r src/* /usr/local/bin/wireguard_tray

echo "Done. Now reboot system :)"
