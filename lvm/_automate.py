import os
import subprocess
x=input("Use existing vg(y/n): ")

vg_name=input("Enter vg name: ")
if x=="y":
    x2=input("Use existing LV (y/n): ")
    lv_name=input("Enter LV name: ")
    lv_size=input("Enter LV size to increase: ")
    if x2=="y":
        os.system("lvextend --size {}G /dev/{}/{} ".format(lv_size,vg_name, lv_name))
    else:
        os.system("lvcreate --size {}G {} {} ".format(lv_size, lv_name, vg_name))
else:
    dev_name=input("Enter device name: ")
    try:
        subprocess.run("vgcreate {} {} ".format(dev_name, vg_name))
    except subprocess.CalledProcessError:
        print ('INVALID')
        break        
    lv_name=input("Enter LV name: ")
    lv_size=input("Enter LV size: ")
    os.system("lvcreate --size {}G {} {} ".format(lv_size, lv_name, vg_name))
