### Python Music Player --- Created by Marvin Kirschner , ITA16a ###

import vlc
import time
import os
import sys

class Player:
    def __init__(self, des, songt, source):
        self.description = des
        self.songtimer = songt
        self.source = source

    def report(self):
        print("Der Song",self.description, "wird nun abgespielt!")

    def abspielen(self):
        self.report
        self.source.play()
        control = input()

        if control == "stop":
            self.source.stop()
            print("Das Lied" ,self.description, "wurde abgebrochen")
        else:
            time.sleep(self.songtimer)
            self.source.stop()
            print("Das Lied" ,self.description, "ist nun zuende! Bitte wählen sie ein anderes Lied aus!")
            

# Klassen

megalovania = Player("Megalovania", 300, vlc.MediaPlayer("file:///Library/Music/01_megalovania.mp3"))

schwifty = Player("Get Schwifty", 62, vlc.MediaPlayer("file:///Library/Music/03_schwifty.mp3"))

fallout = Player("Fallout Theme", 184, vlc.MediaPlayer("file:///Library/Music/04_fallout.mp3"))

countdown = Player("The Final Countdown", 300, vlc.MediaPlayer("file:///Library/Music/05_countdown.mp3"))

imnotgay = Player("I'm not gay", 90, vlc.MediaPlayer("file:///Library/Music/06_imnotgay.mp3"))

halo = Player("Halo - Honest Negotiation Suite", 540, vlc.MediaPlayer("file:///Library/Music/07_halo.mp3"))

portal = Player("Portal - Still Alive", 190, vlc.MediaPlayer("file:///Library/Music/08_portal.mp3"))

waveofdarkness = Player("Wave of Darkness", 195, vlc.MediaPlayer("file:///Library/Music/09_waveofdarkness.mp3"))

gravity = Player("Gravity Falls - Theme", 41, vlc.MediaPlayer("file:///Library/Music/joke_gravity.mp3"))




print("Willkommen in der Musiklounge! Dies ist der PiPlayer, er ermöglicht das abspielen von MP3 Dateien!")
#time.sleep(6)
print("Dieses Programm wurde mithilfe des VLC Python Skriptes und dem VLC Media Player entwickelt")
time.sleep(6)
print("Um dieses Programm zu bedienen sind folgende Befehle erforderlich:")
#time.sleep(2)
print("Mithilfe des Kommandos 'liste' werden alle Musiktitel aufgelistet, welche zur Verfügung stehen")
#time.sleep(3)
print("Durch die Eingabe der Titelnummer wird das jeweilige Musikstück abgespielt.")
#time.sleep(3)
print("Mithilfe von 'hilfe' werden alle Kommandos noch einmal erläutert")
time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')

print("Player startet ....")
time.sleep(2)
print("Willkommen! Bitte geben sie einen Befehl ein!")



try:
    while True:
        ein = input()

        if ein == "hilfe":
            print("Das Kommando 'liste' listet alle Musiktitel auf")
            print("Mit Eingabe der Titelnummer wird das jeweilige Musikstück abgespielt")
            print("Mit 'leeren' wird die Konsole des Programmes geleert")
            print("Mit dem Befehl 'aus' wird das Programm beendet.")

            print("---------------------------------------------------------------------")

            print("Befehle, während ein Musiktitel abgespielt wird:")
            print("Mit dem Befehl 'stop' wird der derzeitige Musiktitel abgebrochen")

            print("---------------------------------------------------------------------")
            print("Mit 'hilfe' werden alle Kommandos noch einmal erläuter")

        elif ein == "liste":
            print("01 = Megalovania")
            print("02 = Derzeit nicht belegt")
            print("03 = Get Schwifty")
            print("04 = Fallout - Theme")
            print("05 = The Final Countdown")
            print("06 = Boyz on Wheelz")
            print("07 = Halo - Honest Negotiation Suite")
            print("08 = Still Alive")
            print("09 = Wave of Darkness")
            print("10 = Gravity Falls - Theme")

        elif ein == "leeren":
            os.system('cls' if os.name == 'nt' else 'clear')


        elif ein == "1":
            megalovania.report()
            megalovania.abspielen()
            
        elif ein == "2":
           print("Hier ist kein Titel vorhanden, such einen anderen aus!")
            
        elif ein == "3":
            schwifty.report()
            schwifty.abspielen()
            
        elif ein == "4":
            fallout.report()
            fallout.abspielen()

        elif ein == "5":
            countdown.report()
            countdown.abspielen()
            
        elif ein == "6":
            imnotgay.report()
            imnotgay.abspielen()
            
        elif ein == "7":
            halo.report()
            halo.abspielen()
            
        elif ein == "8":
            portal.report()
            portal.abspielen()
            
        elif ein == "9":
            waveofdarkness.report()
            waveofdarkness.abspielen()
            
        elif ein == "10":
            gravity.report()
            gravity.abspielen()
            
        elif ein == "aus":
            break

        else:
            print("Wenn sie nicht wissen, was sie eingeben können, tippen sie hilfe ein")
except KeyboardInterrupt:
    sys.out()
