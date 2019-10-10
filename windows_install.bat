@echo off
set /p "setuppath=Enter setup path: "
echo %setuppath%
set "newLocation=%setuppath%\zen-cf-ddns_win.pyw"
echo F | xcopy zen-cf-ddns.py "%newLocation%" /Y /C /R
set "newLocation=%setuppath%\zen-cf-ddns.conf"
echo F | xcopy zen-cf-ddns.conf "%newLocation%" /Y /C /R
set "newLocation=%setuppath%\zen-cf-ddns_win.pyw"
schtasks /create /tn "CloudFlare Update IP" /tr "%newLocation%" /sc onstart