#!/bin/bash
python -m pip install -r requirements.txt
cp zen-cf-ddns.service /lib/systemd/system/zen-cf-ddns.service
mkdir /usr/bin/zen-cf-ddns/
cp zen-cf-ddns.py /usr/bin/zen-cf-ddns/zen-cf-ddns.py
cp zen-cf-ddns.conf /etc/zen-cf-ddns.conf