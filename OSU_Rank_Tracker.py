from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
version = "1"
CHROMEDRIVER = "C:/chromedriver.exe"
os.system('CLS')
try:
    user = open("user_profile.txt", "r")
except:
    user = open("user_profile.txt", "w")
    user.close()
    print("user_profile.txt was missing and now created!")
    print("Please paste profile link inside the file: user_profile.txt")
    time.sleep(8)
    exit()

user_profile = user.read()
user.close()
if user_profile == "":
    print("Please paste profile link inside the file: user_profile.txt")
    time.sleep(8)
    exit()
elif user_profile[:25] != "https://osu.ppy.sh/users/":
    print("Please check again the profile link inside the file: user_profile.txt")
    time.sleep(8)
    exit()
else:
    URL = user_profile
    user.close()

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(CHROMEDRIVER, options=options)


def add_comma(num):
    num = str(num)
    num = num.replace(",","")
    if num[0] == "#":
        num = num.strip("#")
        num = int(num)
        num = ("{:,}".format(num))
        num = "#" + str(num)
        return num
    else:
        num = int(num)
        num = ("{:,}".format(num))
    return num

    
def start_message():
    driver.get(URL)
    startgloball = driver.find_elements_by_class_name("value-display__value")
    startisrael = startgloball[1].text
    startpp = startgloball[4].text
    startglobal = startgloball[0].text
    startglobalint = startgloball[0].text
    startglobalint = startglobalint.replace("#", "")
    startglobalint = startglobalint.replace(",", "")
    startglobalint = int(startglobalint)
    os.system('CLS')
    print("You started rank " + str(add_comma(startglobal)) + " with " + str(add_comma(startpp)) + "pp" + " (In Israel: " + startisrael + ")")
    return startglobalint, startglobal, startisrael, startpp


def check_rank():
    time.sleep(5)
    driver.get(URL)
    checkk = driver.find_elements_by_class_name("value-display__value")
    check = checkk[0].text
    checkisrael = checkk[1].text
    checkpp = checkk[4].text
    checkint = checkk[0].text.replace("#", "")
    checkint = checkint.replace(",", "")
    checkint = int(checkint)
    return check, checkint, checkisrael, checkpp


def rank_change():
    global startglobal
    global startglobalint
    global check
    global checkint
    global nowrank
    global nowpp
    global startisrael
    global checkisrael
    global startpp
    global checkpp

    os.system('CLS')
    print("You started rank " + str(add_comma(startglobal)) + " with " + str(add_comma(startpp)) + "pp" + " (In Israel: " + startisrael + ")")
    print("-------------------------------------------------")
    if nowrank > checkint:
        last_song_up = nowrank - checkint
        print("Congratulations!")
        print("This song made you go " + "+" + str(add_comma(last_song_up)) + " ranks up!")
    if nowrank < checkint:
        last_song_down = checkint - nowrank
        print("OH NO!!!! ")
        print("This song made you go " + "-" + str(add_comma(last_song_down)) + " ranks down!")
    if int(nowpp) < int(checkpp):
        ppup = int(checkpp) - int(nowpp)
        print("This song given you " + "+" + str(add_comma(ppup)) + " pp")
    if int(nowpp) > int(checkpp):
        ppup = int(nowpp) - int(checkpp)
        print("This song cost you " + "-" + str(add_comma(ppup)) + " pp")
    print("You're now rank " + str(add_comma(check)) + " with " + str(add_comma(checkpp)) + "pp"  + " (In Israel: " + checkisrael + ")")
    print("-------------------------------------------------")
    if (startglobalint - checkint) > 0:
        print("Since you started playing today you have risen up " + str(add_comma(startglobalint - checkint)) + " ranks!")
    if (startglobalint - checkint) < 0:
        print("Since you started playing today you have going " + str(add_comma(startglobalint - checkint)) + " ranks down!")
    if (int(checkpp) - int(startpp)) > 0:
        print("Since you started playing today you have risen up " + str(add_comma(int(checkpp) - int(startpp))) + " pp!")
    if (int(checkpp) - int(startpp)) < 0:
        print("Since you started playing today you have lost " + str(add_comma(int(checkpp) - int(startpp))) + "pp")
    nowrank = int(checkint)
    nowpp = int(checkpp)
    file_overwrite("Old", str(startglobal), str(startglobalint), str(check), str(checkint), str(nowrank), str(startisrael), str(checkisrael), str(startpp), str(nowpp))


def file_ex():
    try:
        with open("records.txt") as f:
            file_con = f.read().splitlines()
        f.close()
    except:
        os.system('CLS')
        print("Hello new user!")
        time.sleep(1)
        file_con = file_overwrite("New", "0", "0", "0", "0", "0", "0", "0", "0", "0")
    return file_con


def file_overwrite(neww, startglobalt, startglobalintt, checkk, checkintt, nowrankk, startisraell, checkisraell, startppp, checkppp):
    f = open("records.txt", "w")
    f.write("new:\n")
    f.write(str(neww) + "\n")
    f.write("startglobal:\n")
    f.write(str(startglobalt) + "\n")
    f.write("startglobalint:\n")
    f.write(str(startglobalintt) + "\n")
    f.write("check:\n")
    f.write(str(checkk) + "\n")
    f.write("checkint:\n")
    f.write(str(checkintt) + "\n")
    f.write("nowrank:\n")
    f.write(str(nowrankk) + "\n")
    f.write("startisrael:\n")
    f.write(str(startisraell) + "\n")
    f.write("checkisrael:\n")
    f.write(str(checkisraell) + "\n")
    f.write("startpp:\n")
    f.write(str(startppp) + "\n")
    f.write("checkpp:\n")
    f.write(str(checkppp) + "\n")
    f.close()
    with open("records.txt") as f:
        file_con = f.read().splitlines()
    f.close()
    return file_con


file = file_ex()
os.system('CLS')
print("Welcome to OSU Rank Tracker! " + "Version " + version )
if file[1] == "Old":
    user_in = input("Reset stats? (Y/N):")
    while not (user_in == "Y" or user_in == "N" or user_in == "y" or user_in == "n"):
        os.system('CLS')
        print("Welcome to OSU Rank Tracker!")
        user_in = input("Reset stats? (Y/N):")
    if user_in == "Y" or user_in == "y" :
        os.system('CLS')
        print("Restting stats...")
        time.sleep(2)
        os.system('CLS')
        file_overwrite("New", "0", "0", "0", "0", "0", "0", "0", "0", "0")
        startglobal_msg = start_message()
        startglobal = startglobal_msg[1]
        startglobalint = int(startglobal_msg[0])
        startisrael = startglobal_msg[2]
        nowrank = int(startglobal_msg[0])
        startpp = int(startglobal_msg[3])
        nowpp = int(startglobal_msg[3])
    else:
        os.system('CLS')
        print("Keeping the stats...")
        time.sleep(2)
        os.system('CLS')
        startglobal = file[3]
        startglobalint = int(file[5])
        startisrael = file[13]
        nowrank = int(file[11])
        startpp = int(file[17])
        nowpp = int(file[19])
        print("You started rank " + str(add_comma(startglobal)) + " with " + str(add_comma(startpp)) + "pp" + " (In Israel: " + startisrael + ")")
else:
    startglobal_msg = start_message()
    startglobal = startglobal_msg[1]
    startglobalint = int(startglobal_msg[0])
    startisrael = startglobal_msg[2]
    nowrank = int(startglobal_msg[0])
    startpp = int(startglobal_msg[3])
    nowpp = int(startglobal_msg[3])


while True:
    time.sleep(2)
    check_msg = check_rank()
    check = check_msg[0]
    checkint = check_msg[1]
    checkisrael = check_msg[2]
    checkpp = check_msg[3]

    if nowrank != checkint:
        os.system('CLS')
        print("New rank detected! Updating...")
        time.sleep(2)
        rank_change()


