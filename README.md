# About
Dynamic DNS client based on CloudFlare API.
Can be used as alternative to ddclient.
# How to install and use
## Docker
1. Clone repo: `git clone https://github.com/DzenDyn/zen-cf-ddns.git`
2. Go to repo dir: `cd zen-cf-ddns`
3. Edit configuration file zen-cf-ddns.conf
4. Run `docker build .`

or visit [docker hub](https://hub.docker.com/repository/docker/dzendyn/zen-cf-ddns "docker hub")  

## Linux install
1. Clone repo: `git clone https://github.com/DzenDyn/zen-cf-ddns.git`
2. Go to repo dir: `cd zen-cf-ddns`
3. Run ./install.sh with sudo:

```
chmod +x install.sh
sudo ./install.sh
```

4. Change settings in /etc/zen-cf-ddns.conf: `sudoedit /etc/zen-cf-ddns.conf `

This is a JSON configuration file, so its easy to configure.

Now you can start, stop, restart or status with:
```
sudo systemctl start zen-cf-ddns.service
sudo systemctl stop zen-cf-ddns.service
sudo systemctl restart zen-cf-ddns.service
sudo systemctl status zen-cf-ddns.service

or

sudo service zen-cf-ddns start
sudo service zen-cf-ddns stop
sudo service zen-cf-ddns restart
sudo service zen-cf-ddns status

```

## Windows install
1. Clone repo: `git clone https://github.com/DzenDyn/zen-cf-ddns.git`
If you do not have git installed, install it or simply download the repository as a zip file.

2. Install the Python3 from https://python.org/, during installation, add python to path.

3. Go to repo dir and run cmd or powershell there as administrator.

4. Update pip: `python -m pip install --upgrade pip`

5. Install requirements: `python -m pip install -r requirements.txt`

6. Run windows_install.bat

During the installation, a task will be created in the scheduler, which will run the script when the system starts.

7. Remember to edit the configuration file before run the script.
This is a JSON configuration file, so its easy to configure.


To run the script, double-click zen-cf-ddns-win.pyw and select run using python.
To stop or apply new conf you must firstly kill pythonw.exe with taskmanager or `taskkill /im pythonw.exe /f`

---
The project was based on a library [python-cloudflare](https://github.com/cloudflare/python-cloudflare "python-cloudflare") and uses Cloudflare API.
