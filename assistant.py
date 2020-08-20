import pyttsx3 as tts
import os
import time
import platform
import subprocess

if(platform.system() == "Windows"):
    cmd = "where"
else:
    cmd = "which"

print("\n Hello Sir ! Welcome ! I am Centaurus, your virtual assistant")
tts.speak("Hello Sir ! Welcome ! I am Centaurus, your virtual assistant")

while True:
    tts.speak("Tell me your requirements")
    txt = input("\n Tell me your Requirements: ").lower()

    if("do not" in txt) or ("don't" in txt) or ("dont" in txt):
        tts.speak("Not opening the application")
        time.sleep(1)
        continue

    elif (("thank you" in txt) or ("exit" in txt)):
        tts.speak("Thanks for using me")
        break

    elif("stop" in txt):
        tts.speak("Do you want to stop a process ? ")
        kill = input("\n Do you want to stop a process ? ")

        if(kill.lower() == "yes"):
            if("notepad" in txt):
                result = os.system("taskkill /im notepad.exe /f")
                if (result == 0):
                    tts.speak("All notepads should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("chrome" in txt):
                result = os.system("taskkill /im chrome.exe /f")
                if (result == 0):
                    tts.speak("All chrome browser should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("wordpad" in txt):
                result = os.system("taskkill /im wordpad.exe /f")
                if (result == 0):
                    tts.speak("All wordpad should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("firefox" in txt):
                result = os.system("taskkill /im firefox.exe /f")
                if (result == 0):
                    tts.speak("All firefox should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif (("ms-word" in txt) or ("word" in txt)):
                result = os.system("taskkill /im winword.exe /f")
                if (result == 0):
                    tts.speak("All ms-word should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("media player" in txt):
                result = os.system("taskkill /im wmplayer.exe /f")
                if (result == 0):
                    tts.speak("All media player should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("clock" in txt):
                result = os.system("taskkill /im msclock.exe /f")
                if (result == 0):
                    tts.speak("All clocks should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("calulator" in txt):
                result = os.system("taskkill /im Calculator.exe /f")
                if (result == 0):
                    tts.speak("All calculators should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("calendar" in txt):
                result = os.system("taskkill /im HxCalendarAppImm.exe /f")
                if (result == 0):
                    tts.speak("All calendars should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("camera" in txt):
                result = os.system(
                    "taskkill /im WindowsCamera.exe /f")
                if (result == 0):
                    tts.speak("All camera should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("paint" in txt):
                result = os.system(
                    "taskkill /im mspaint.exe /f")
                if (result == 0):
                    tts.speak("All paint should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("powerpoint" in txt):
                result = os.system(
                    "taskkill /im POWERPNT.exe /f")
                if (result == 0):
                    tts.speak("All Powerpoint should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("excel" in txt):
                result = os.system(
                    "taskkill /im EXCEL.exe /f")
                if (result == 0):
                    tts.speak("All excel should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

            elif("access" in txt):
                result = os.system(
                    "taskkill /im MSACCESS.exe /f")
                if (result == 0):
                    tts.speak("All Access should be dead now...")
                else:
                    tts.speak("Error executing taskkill command !!!")

        elif(kill.lower() == "no"):
            tts.speak("Manually you can close it later then.")

    elif(("run" in txt) or ("execute" in txt) or ("open" in txt) or ("show" in txt) or ("start" in txt)):

        if("browser" in txt):
            tts.speak("Which browser you want to open : ")
            browser = input(" Which browser you want to open : ")

            if("chrome" in browser):
                rc = subprocess.call([cmd, 'chrome'])
                if (rc == 0):
                    tts.speak("Opening Google Chrome")
                    os.system("start chrome")
                    time.sleep(1)
                else:
                    tts.speak("Chrome application is not present")

            elif("firefox" in browser):
                rc = subprocess.call([cmd, 'firefox'])
                if(rc == 0):
                    tts.speak("Opening Firefox")
                    os.system("start firefox")
                    time.sleep(1)
                else:
                    tts.speak("Firefox application is not present")

        elif("text editor" in txt):
            tts.speak("Which text editor you want to open: ")
            editor = input(" Which text editor you want to open: ")

            if("notepad" in editor):
                tts.speak("Opening Notepad")
                os.system("start notepad")
                time.sleep(1)

            elif("wordpad" in editor):
                tts.speak("Opening Wordpad")
                os.system("start wordpad")
                time.sleep(1)

            elif (("ms-word" in editor) or ("microsoft office word" in editor) or ("word" in editor)):
                tts.speak("Opening Microsoft Office Word")
                os.system("start winword")
                time.sleep(1)

        elif("media player" in txt):
            tts.speak(" Which media player you want to open: ")
            player = input("Which media player you want to open: ")

            if("windows media player" in player):
                tts.speak("Opening Windows Media Player")
                os.system("start wmplayer")
                time.sleep(1)

            elif("vlc" in player):
                rc = subprocess.call([cmd, 'vlc'])
                if(rc == 0):
                    tts.speak("Opening VLC")
                    os.system("start vlc")
                    time.sleep(1)
                else:
                    tts.speak("VLC application is not present")

        elif("clock" in txt):
            tts.speak("Opening alamrs and clock")
            os.system("start ms-clock:")
            time.sleep(1)

        elif("available networks" in txt):
            tts.speak("Showing available Networks")
            os.system("start ms-availablenetworks:")
            time.sleep(1)

        elif (("calculator" in txt) or ("calc" in txt)):
            tts.speak("Opening Calculator")
            os.system("start calculator:")
            time.sleep(1)

        elif("calendar" in txt):
            tts.speak("Opening Calendar")
            os.system("start outlookcal:")
            time.sleep(1)

        elif("camera" in txt):
            tts.speak("Starting Camera")
            os.system("start microsoft.windows.camera:")
            time.sleep(1)

        elif("paint" in txt):
            tts.speak("Opening paint")
            os.system("start mspaint")
            time.sleep(1)

        elif("photos" in txt):
            tts.speak("Opening photos")
            os.system("start ms-photos:")
            time.sleep(1)

        elif("snipping tool" in txt):
            tts.speak("Opening Snipping Tool")
            os.system("start SnippingTool")
            time.sleep(1)

        elif("settings" in txt):
            tts.speak("Opening settings")
            os.system("start ms-settings:")
            time.sleep(1)

        elif("voice recorder" in txt):
            tts.speak("Opening voice recorder")
            os.system("start ms-callrecording:")
            time.sleep(1)

        elif("weather" in txt):
            tts.speak("Showing the current weather conditions")
            os.system("start bingweather:")
            time.sleep(1)

        elif("windows defender" in txt):
            tts.speak("Opening Windows Defender")
            os.system("start windowsdefender")
            time.sleep(1)

        elif (("ms-excel" in txt) or ("microsoft office excel" in txt) or ("excel" in txt)):
            tts.speak("Opening Microsoft Office Excel")
            os.system("start excel")
            time.sleep(1)

        elif (("ms-access" in txt) or ("microsoft office access" in txt) or ("access" in txt)):
            tts.speak("Opening Microsoft Office Access")
            os.system("start msaccess")
            time.sleep(1)

        elif("pdf viewer" in txt):
            tts.speak("Opening Adobe Acrobat Reader")
            os.system("start AcroRd32")
            time.sleep(1)

        elif (("ms-powerpoint" in txt) or ("microsoft office powerpoint" in txt) or ("powerpoint" in txt)):
            tts.speak("Opening Microsoft Office Powerpoint")
            os.system("start powerpnt")
            time.sleep(1)

        elif (("visual studio code" in txt) or ("vs code" in txt)):
            tts.speak("Opening Visual Studio Code")
            os.system("start Code-Insiders")
            time.sleep(1)
