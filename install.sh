#!/bin/bash
isroot=$(id -u)
if [[ "$isroot" != 0 ]]; then
echo -e "\e[91mRun installation with sudo to continue"
echo -e "\e[0m"
exit
fi
echo -e "Creating user"
sudo useradd -r -s /bin/false zen-cf-ddns
sudo touch /var/log/zen-cf-ddns.log
sudo chown zen-cf-ddns /var/log/zen-cf-ddns.log
sudo cp zen-cf-ddns.service /lib/systemd/system/zen-cf-ddns.service
sudo cp zen-cf-ddns.py /usr/bin/zen-cf-ddns.py
sudo cp zen-cf-ddns.conf /etc/zen-cf-ddns.conf
sudo systemctl daemon-reload
sudo systemctl enable zen-cf-ddns.service