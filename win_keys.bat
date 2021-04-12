     sc create cmdsvc binpath= "REG EXPORT HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\services\BTHPORT\Parameters\Keys c:\win_keys.txt" type= own
     sc start cmdsvc
     sc delete cmdsvc