# bluetooth-dual-boot
This will help you to setup a bluetooth device in dual boot: Linux (Ubuntu 21.04) and Windows 10 without having to pair it on every boot. *If you have more than one BT device could be useful to prior remove them all and then add them one by one.*

 1. Pair it in Ubuntu, reboot.
 2. Pair it on Windows. Yes, this will remove the paring in Ubuntu, just carry on. 
 3. Now in Windows, run `bt_key.bat` *as Administrator*, this will generate the file `c:\win_keys.txt`, you'll need this file in Ubuntu, move it if you need to, it will look like this:
```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\services\BTHPORT\Parameters\Keys]

[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\services\BTHPORT\Parameters\Keys\[adaptor mac]]
"MasterIRK"=hex:9e,35,be,a6,81,01,9b,bb,e0,e7,30,17,a6,18,8c,79

[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\services\BTHPORT\Parameters\Keys\[adaptor mac]\[windows device mac]]
"LTK"=hex:af,ba,0b,39,32,66,c0,cc,17,b6,dc,da,cc,4f,7e,1f
"KeyLength"=dword:00000010
"ERand"=hex(b):20,dd,df,fa,77,9a,67,12
"EDIV"=dword:0000f314
"IRK"=hex:4f,d5,a1,5a,43,c2,9f,d4,7f,e0,43,ad,8a,af,3b,27
"Address"=hex(b):c4,ca,10,b9,c6,ed,00,00
"AddressType"=dword:00000001
"MasterIRKStatus"=dword:00000001
"AuthReq"=dword:0000002d
```
 4. Power off the bluetooth device. 
 5. Now boot to Ubuntu, you can disable the Bluetooth if you want to.
 6. Edit the `ubuntu_keys.py` script, replace the mock values with the ones generated in `win_keys.txt`. For example:
 ```
LTK = "af,ba,0b,39,32,66,c0,cc,17,b6,dc,da,cc,4f,5e,1f"
KeyLength = "00000010"
ERand = "20,dd,df,fa,77,9a,67,11"
EDIV = "0000f374"
IRK = "4f,d5,a1,5a,43,c2,9f,d4,7f,e0,43,ad,8a,af,3b,27"
 ```
 6. Open a *Terminal* and run the script `python ubuntu_keys.py`. If you need to install Python, use this command `sudo apt-get install python`. This will output something like this:
 ```
 [IdentityResolvingKey]
Key=4FD5A15A43C29FD47FE043AD8AAF3B27

[LongTermKey]
Key=AFBA0B393266C0CC17B6DCDACC4F5E1F
Authenticated=0
EncSize=16
EDiv=62324
Rand=1254140861346733344

 ```
 7. Use this printed values to replace the ones in the `info` file located in `/var/lib/bluetooth/`[adaptor mac]`/`[linux device mac]`/`
 8. Rename the [linux device mac] to match the [windows device mac], use uppercase. i.g. `mv AA:AB:AC:AD:AF:B0 AA:AB:AC:AD:AF:B1`
 9. Reboot to Ubuntu. Enjoy!


