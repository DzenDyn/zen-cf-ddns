#!/bin/bash
isroot=$(id -u)
if [[ "$isroot" != 0 ]]; then
echo -e "\e[91mRun installation with sudo to continue"
echo -e "\e[0m"
exit
fi
sudo python3 -m venv /usr/lib/zen-cf-ddns
source /usr/lib/zen-cf-ddns/bin/activate
python -m pip install -upgrade pip
python -m pip install -r requirements.txt
sudo cp zen-cf-ddns.service /lib/systemd/system/zen-cf-ddns.service
sudo cp zen-cf-ddns.py /usr/bin/zen-cf-ddns.py
sudo cp zen-cf-ddns.conf /etc/zen-cf-ddns.conf
sudo systemctl daemon-reload
sudo systemctl enable zen-cf-ddns.service