## How to install and use

1. Clone repo:

`git clone https://github.com/DzenDyn/zen-cf-ddns.git`

2. Install the python3-pip if you do not have it:

`sudo apt install python3-pip`

3. Go to created folder and make the install.sh file executable:

`cd zen-cf-ddns`

`chmod +x install.sh`

4. Run install.sh:

`sudo ./install.sh`

5. Reload systemd using command: 

`sudo systemctl daemon-reload`

6. Enable auto start using command:

`sudo systemctl enable zen-cf-ddns.service`

7. Change settings in /etc/zen-cf-ddns.conf:

`
sudoedit /etc/zen-cf-ddns.conf
`

This is a JSON configuration file, so its easy to configure.

The log is written to /var/log/zen-cf-ddns.log.

The project was based on a library [python-cloudflare](https://github.com/cloudflare/python-cloudflare "python-cloudflare") and uses Cloudflare API.
