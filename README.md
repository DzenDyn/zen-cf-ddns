## How to install and use

1. Clone repo:

`git clone https://github.com/DzenDyn/zen-cf-ddns.git`

2. Make the install.sh file executable:

`chmod +x install.sh`

3. Run install.sh:

`sudo ./install.sh`

4. Reload systemd using command: 

`systemctl daemon-reload`

5. Enable auto start using command:

`systemctl enable zen-cf-ddns.service`

6. Change settings in /etc/zen-cf-ddns.conf:

`
sudoedit /etc/zen-cf-ddns.conf
`

This is a JSON configuration file, so its easy to configure.

The log is written to /var/log/zen-cf-ddns.log.

The project was based on a library [python-cloudflare](https://github.com/cloudflare/python-cloudflare "python-cloudflare") and uses Cloudflare API.
