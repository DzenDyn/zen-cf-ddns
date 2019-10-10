## How to install and use

1. Clone repo:

`git clone https://github.com/DzenDyn/zen-cf-ddns.git`

2. Install the python3 and python3-pip if you do not have it:

```
sudo apt install python3
sudo apt install python3-pip
```

3. Go to repo dir:

`cd zen-cf-ddns`

4. Install requirements:

`python3 -m pip install -r requirements.txt`

5. Run ./install.sh with sudo:

```
chmod +x install.sh
sudo ./install.sh
```

9. Change settings in /etc/zen-cf-ddns.conf:

`
sudoedit /etc/zen-cf-ddns.conf
`

This is a JSON configuration file, so its easy to configure.
Do not forget to specify a place to store logs. The user must have permissions to write to this directory.

Now you can start, stop, restart or status with:
```
sudo service zen-cf-ddns start
sudo service zen-cf-ddns stop
sudo service zen-cf-ddns restart
sudo service zen-cf-ddns status

```

The project was based on a library [python-cloudflare](https://github.com/cloudflare/python-cloudflare "python-cloudflare") and uses Cloudflare API.
