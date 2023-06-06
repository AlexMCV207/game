import os
from colorama import Fore, Back
import random

def printBlack(data):
    print(Fore.BLACK,data,end="",sep="")

def printCyan(data):
    print(Fore.CYAN,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

gracz = 0
p1hp = 0
p2hp = 0

def shellAPdmg(hp,dmg,dfn):
    a = random.randint(1,5)
    if(a == 1):
        print("Non-penetration!")
    if(a > 1 and a <= 5):
        if(dmg <= dfn):
            print("Non-penetration!")
        else:
            if(hp <= dmg):
                hp = 0
            hp = hp - dmg + dfn
            if(gracz == 1):
                p2hp = hp
                return p2hp
            if(gracz == -1):
                p1hp == hp
                return p1hp
            print("We dealt",dmg - dfn,"damage!")

def shellHEdmg(hp,dmg,dfn,wsp):
    if(wsp <= dfn):
        print("Non-penetration!")
    else:
        if(hp <= dmg):
            hp = 0
        dmg = wsp - dfn
        dmg = dmg * 8
        hp = hp - dmg
        if(gracz == 1):
            p2hp = hp
            return p2hp
        if(gracz == -1):
            p1hp == hp
            return p1hp
        print("We dealt",dmg,"damage!")

def shellAPCRdmg(hp,dmg,dfn):
    if(dmg <= dfn):
        if(hp <= dmg):
            hp = 0
        dmg = dmg - dfn
        dmg = dmg * 0,5
        hp = hp - dmg
        if(gracz == 1):
            p2hp = hp
            return p2hp
        if(gracz == -1):
            p1hp == hp
            return p1hp
        print("We dealt",dmg,"damage!")

hp1 = 100
dmg1 = 20
def1 = 5
a = shellAPCRdmg(hp1,dmg1,def1)
print(a)
bb = input

def shellHEATFSdmg(hp,dmg,dfn):
    if(hp <= dmg):
        hp = 0
    hp = hp - dmg
    if(gracz == 1):
        p2hp = hp
        return p2hp
    if(gracz == -1):
        p1hp == hp
        return p1hp
    print("We dealt",dmg,"damage!")


def shellHESHdmg(hp,dmg,dfn,wsp):
    if(wsp <= dfn):
        print("Non-penetration!")
    else:
        if(hp <= dmg):
            hp = 0
        dmg = wsp - dfn
        dmg = dmg * 11
        hp = hp - dmg
        if(gracz == 1):
            p2hp = hp
            return p2hp
        if(gracz == -1):
            p1hp == hp
            return p1hp
        print("We dealt",dmg,"damage!")
    
def screenXO(screen):
    os.system('cls')

    corners = {
               "upperLeft":     "┌",
               "upperRight":    "┐",
               "mediumLeft":    "├",
               "mediumRight":   "┤",
               "bottomLeft":    "└",
               "bottomRight":   "┘",
               "upperMid":      "┬",
               "mediumMid":     "┼",
               "bottomMid":     "┴"
              }
    lines =   {
               "vertical": "│",
               "horizontal": "─"
              }
    
    size = len(screen)             

    verticalLine = [lines["horizontal"]*3]*size       
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["mediumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
   
    printBlack(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printBlack(lines["vertical"])
        for j in row:
            if(j>0): printGreen(" ¤ ")
            elif j<0: printCyan(" ¤ ")
            else: printBlack("   ")
            printBlack(lines["vertical"])            
        print()
        if(i < size-1): printBlack(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")
    
    printBlack(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")



if __name__ == "__main__":
    zp1 = 0
    zp2 = 0
    zp3 = 11
    zp4 = 11
    rozmiar = 12
    dane = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)
    dane[zp1][zp2] = 1
    dane[zp3][zp4] = -1
    gracz = 1

    print("┌────────────────────────────────────────────┐")
    print("│ Absolutely accurate tank warfare simulator │")
    print("└────────────────────────────────────────────┘")
    print("┌──────────────────┐")
    print("│    (s) Start     │")
    print("└──────────────────┘")
    print("┌──────────────────┐")
    print("│ (h) How to play? │")
    print("└──────────────────┘")
    o1 = input()
    while True:
        try:
            if(o1 == "s" or o1 == "h"):
                break
        except:
            pass
    if(o1 == "h"):
        print("")
    if(o1 == "s"):
        print("┌───────────────────────────────┐")
        print("│ Player 1, Choose your vehicle │")
        print("└───────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 1. Pzkpfw. VI Tiger Ausf. H1 │")
        print("│ health: 1150                 │")
        print("│ damage: 130                  │")
        print("│ defense: 35                  │")
        print("│ HE/HESH factor: 20           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ AP                           │")
        print("│ HE                           │")
        print("│ APCR                         │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 2. M36B2                     │")
        print("│ health: 810                  │")
        print("│ damage: 160                  │")
        print("│ defense: 10                  │")
        print("│ HE/HESH factor: 45           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ AP                           │")
        print("│ HE                           │")
        print("│ APCR                         │")
        print("│ HEATFS                       │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 3. FV4005                    │")
        print("│ health: 675                  │")
        print("│ damage: 255                  │")
        print("│ defense: 10                  │")
        print("│ HE/HESH factor: 65           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ HESH                         │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 4. IS 2                      │")
        print("│ health: 985                  │")
        print("│ damage: 145                  │")
        print("│ defense: 45                  │")
        print("│ HE/HESH factor: 30           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ AP                           │")
        print("│ HE                           │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 5. ELC bis                   │")
        print("│ health: 460                  │")
        print("│ damage: 180                  │")
        print("│ defense: 10                  │")
        print("│ HE/HESH factor: 55           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ HEATFS                       │")        
        print("│ HE                           │")
        print("└──────────────────────────────┘")
        o2 = input()
        while True:
            try:
                if(o2 == "1" or o2 == "2" or o2 == "3" or o2 == "4" or o2 == "5"):
                    break
            except:
                pass
        if(o2 == "1"):
            p1hp = 1150
            p1dmg = 130
            p1def = 35
            fact = 20
            p1shell1 = "AP"
            p1shell2 = "HE"
            p1shell3 = "APCR"
            p1shell4 = ""
        if(o2 == "2"):
            p1hp = 810
            p1dmg = 160
            p1def = 10
            fact = 45
            p1shell1 = "AP"
            p1shell2 = "HE"
            p1shell3 = "APCR"
            p1shell4 = "HEATFS"
        if(o2 == "3"):
            p1hp = 675
            p1dmg = 255
            p1def = 10
            fact = 65
            p1shell1 = "HESH"
            p1shell2 = ""
            p1shell3 = ""
            p1shelll4 = ""
        if(o2 == "4"):
            p1hp = 985
            p1dmg = 145
            p1def = 45
            fact = 30
            p1shell1 = "AP"
            p1shell2 = "HE"
            p1shell3 = ""
            p1shell4 = ""
        if(o2 == "5"):
            p1hp = 460
            p1dmg = 180
            p1def = 10
            fact = 55
            p1shell1 = "HEATFS"
            p1shell2 = "HE"
            p1shell3 = ""
            p1shell4 = ""

        print("┌───────────────────────────────┐")
        print("│ Player 2, Choose your vehicle │")
        print("└───────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 1. Pzkpfw. VI Tiger Ausf. H1 │")
        print("│ health: 1150                 │")
        print("│ damage: 130                  │")
        print("│ defense: 35                  │")
        print("│ HE/HESH factor: 20           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ AP                           │")
        print("│ HE                           │")
        print("│ APCR                         │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 2. M36B2                     │")
        print("│ health: 810                  │")
        print("│ damage: 160                  │")
        print("│ defense: 10                  │")
        print("│ HE/HESH factor: 45           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ AP                           │")
        print("│ HE                           │")
        print("│ APCR                         │")
        print("│ HEATFS                       │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 3. FV4005                    │")
        print("│ health: 675                  │")
        print("│ damage: 255                  │")
        print("│ defense: 10                  │")
        print("│ HE/HESH factor: 65           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ HESH                         │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 4. IS 2                      │")
        print("│ health: 985                  │")
        print("│ damage: 145                  │")
        print("│ defense: 45                  │")
        print("│ HE/HESH factor: 30           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ AP                           │")
        print("│ HE                           │")
        print("└──────────────────────────────┘")
        print("┌──────────────────────────────┐")
        print("│ 5. ELC bis                   │")
        print("│ health: 460                  │")
        print("│ damage: 180                  │")
        print("│ defense: 10                  │")
        print("│ HE/HESH factor: 55           │")
        print("│                              │")
        print("│ Shells:                      │")
        print("│ HEATFS                       │")        
        print("│ HE                           │")
        print("└──────────────────────────────┘")
        o3 = input()
        while True:
            try:
                if(o3 == "1" or o3 == "2" or o3 == "3" or o3 == "4" or o3 == "5"):
                    break
            except:
                pass
        if(o3 == "1"):
            p2hp = 1150
            p2dmg = 130
            p2def = 35
            fact = 20
            p2shell1 = "AP"
            p2shell2 = "HE"
            p2shell3 = "APCR"
            p2shell4 = ""
        if(o3 == "2"):
            p2hp = 810
            p2dmg = 160
            p2def = 10
            fact = 45
            p2shell1 = "AP"
            p2shell2 = "HE"
            p2shell3 = "APCR"
            p2shell4 = "HEATFS"
        if(o3 == "3"):
            p2hp = 675
            p2dmg = 255
            p2def = 10
            fact = 65
            p2shell1 = "HESH"
            p2shell2 = ""
            p2shell3 = ""
            p2shelll4 = ""
        if(o3 == "4"):
            p2hp = 985
            p2dmg = 145
            p2def = 45
            fact = 30
            p2shell1 = "AP"
            p2shell2 = "HE"
            p2shell3 = ""
            p2shell4 = ""
        if(o3 == "5"):
            p2hp = 460
            p2dmg = 180
            p2def = 10
            fact = 55
            p2shell1 = "HEATFS"
            p2shell2 = "HE"
            p2shell3 = ""
            p2shell4 = ""
        
        while True:
            while(p1hp != 0 and p2hp != 0):
                p1t = 0
                p1m = 0
                p1f = 0
                p2t = 0
                p2m = 0
                p2f = 0
                while(p1t < 2 and p2t < 2):
                        

                    screenXO(dane)

                    if(gracz == 1):
                        printGreen("Player 1\n")
                        print("Health: ",p1hp)
                        print("Damage: ",p1dmg)
                        print("Protection: ",p1def)
                        print()
                    else: 
                        printCyan("Player 2\n")
                        print("Health: ",p2hp)
                        print("Damage: ",p2dmg)
                        print("Protection:",p2def)
                        print()

                    print("Choose your action: \n")
                    print("(m) Move")
                    print("(f) Fire")
                    print("(t) Finish turn")
                    
                    while True:
                        try:   
                            a = input()
                            if(a == "m" or a == "f" or a == "t"):
                                break
                        except:
                            pass
                    if(a == "m"):
                        if not (p1m == 0 and p2m == 0):
                            print("You can't move twice!")
                        else:

                            while True:
                                try:
                                    x = int(input("Input x coordinate: "))
                                    y = int(input("Input y coordinate: "))
                                    if(x <= 12):  
                                        if(y <= 12):
                                                if(gracz == 1):
                                                    if not (x == zp3 and y == zp4):
                                                        dane[zp1][zp2] = 0
                                                        zp1 = x
                                                        zp2 = y
                                                        dane[y][x] = gracz
                                                        p1t += 1
                                                if(gracz == -1):
                                                    if not (x == zp1 and y == zp2):
                                                        dane[zp3][zp4] = 0
                                                        zp3 = x
                                                        zp4 = y
                                                        dane[y][x] = gracz
                                                        p2t += 1
                                                if not (zp1 == zp3 and zp2 == zp4):
                                                    break
                                except:
                                    print("You can't move to a square that's already occupied!")
                                    pass

                    


                    if(a == "f"):
                        if not (p1f == 0 and p2f == 0):
                            print("You can't fire twice!")
                        else:
                            p1f += 1
                            p2f += 1
                            print("Choose the player you want to attack")
                            if(gracz == 1):
                                p1t += 1
                                print("(1) Player 2")
                                o4 = input()
                                while True:
                                    try:
                                        if(o4 == "1"):
                                            break
                                    except:
                                        pass
                                print("Choose the shell")
                                if(p1shell1 != ""):
                                    print("(1)",p1shell1)
                                if(p1shell2 != ""):
                                    print("(2)",p1shell2)
                                if(p1shell3 != ""):
                                    print("(3)",p1shell3)
                                if(p1shell4 != ""):
                                    print("(4)",p1shell4)
                                o5 = input()
                                while True:
                                    try:
                                        if(o5 == "1" or o5 == "2" or o5 == "3" or o5 == "4"):
                                            break
                                    except:
                                        pass
                                if(o5 == "1"):
                                    if(p1shell1 == "AP"):
                                        p2hp = shellAPdmg(p2hp,p1dmg,p2def)
                                    if(p1shell1 == "HE"):
                                        p2hp = shellHEdmg(p2hp,p1dmg,p2def,fact)
                                    if(p1shell1 == "APCR"):
                                        p2hp = shellAPCRdmg(p2hp,p1dmg,p2def)
                                    if(p1shell1 == "HEATFS"):
                                        p2hp = shellHEATFSdmg(p2hp,p1dmg,p2def)
                                    if(p1shell1 == "HESH"):
                                        shellHESHdmg(p2hp,p1dmg,p2def,fact)
                                if(o5 == "2"):
                                    if(p1shell2 == "AP"):
                                        p2hp = shellAPdmg(p2hp,p1dmg,p2def)
                                    if(p1shell2 == "HE"):
                                        p2hp = shellHEdmg(p2hp,p1dmg,p2def,fact)
                                    if(p1shell2 == "APCR"):
                                        p2hp = shellAPCRdmg(p2hp,p1dmg,p2def)
                                    if(p1shell2 == "HEATFS"):
                                        p2hp = shellHEATFSdmg(p2hp,p1dmg,p2def)
                                    if(p1shell2 == "HESH"):
                                        p2hp = shellHESHdmg(p2hp,p1dmg,p2def,fact)
                                if(o5 == "3"):
                                    if(p1shell3 == "AP"):
                                        p2hp = shellAPdmg(p2hp,p1dmg,p2def)
                                    if(p1shell3 == "HE"):
                                        p2hp = shellHEdmg(p2hp,p1dmg,p2def,fact)
                                    if(p1shell3 == "APCR"):
                                        p2hp = shellAPCRdmg(p2hp,p1dmg,p2def)
                                    if(p1shell3 == "HEATFS"):
                                        p2hp = shellHEATFSdmg(p2hp,p1dmg,p2def)
                                    if(p1shell3 == "HESH"):
                                        p2hp = shellHESHdmg(p2hp,p1dmg,p2def,fact)
                                if(o5 == "4"):
                                    if(p1shell4 == "AP"):
                                        p2hp = shellAPdmg(p2hp,p1dmg,p2def)
                                    if(p1shell4 == "HE"):
                                        p2hp = shellHEdmg(p2hp,p1dmg,p2def,fact)
                                    if(p1shell4 == "APCR"):
                                        p2hp = shellAPCRdmg(p2hp,p1dmg,p2def)
                                    if(p1shell4 == "HEATFS"):
                                        p2hp = shellHEATFSdmg(p2hp,p1dmg,p2def)
                                    if(p1shell4 == "HESH"):
                                        p2hp = shellHESHdmg(p2hp,p1dmg,p2def,fact)

                            if(gracz == -1):
                                p2t += 1
                                print("(1) Player 2")
                                o4 = input()
                                while True:
                                    try:
                                        if(o4 == "1"):
                                            break
                                    except:
                                        pass       
                                print("Choose the shell")
                                if(p2shell1 != ""):
                                    print("(1)",p2shell1)
                                if(p2shell2 != ""):
                                    print("(2)",p2shell2)
                                if(p2shell3 != ""):
                                    print("(3)",p2shell3)
                                if(p2shell4 != ""):
                                    print("(4)",p2shell4)
                                o5 = input()
                                while True:
                                    try:
                                        if(o5 == "1" or o5 == "2" or o5 == "3" or o5 == "4"):
                                            break
                                    except:
                                        pass
                                if(o5 == "1"):
                                    if(p2shell1 == "AP"):
                                        p1hp = shellAPdmg(p1hp,p2dmg,p1def)
                                    if(p2shell1 == "HE"):
                                        p1hp = shellHEdmg(p1hp,p2dmg,p1def,fact)
                                    if(p2shell1 == "APCR"):
                                        p1hp = shellAPCRdmg(p1hp,p2dmg,p1def)
                                    if(p2shell1 == "HEATFS"):
                                        p1hp = shellHEATFSdmg(p1hp,p2dmg,p1def)
                                    if(p2shell1 == "HESH"):
                                        p1hp = shellHESHdmg(p1hp,p2dmg,p1def,fact)
                                if(o5 == "2"):
                                    if(p2shell2 == "AP"):
                                        p1hp = shellAPdmg(p1hp,p2dmg,p1def)
                                    if(p2shell2 == "HE"):
                                        p1hp = shellHEdmg(p1hp,p2dmg,p1def,fact)
                                    if(p2shell2 == "APCR"):
                                        p1hp = shellAPCRdmg(p1hp,p2dmg,p1def)
                                    if(p2shell2 == "HEATFS"):
                                        p1hp = shellHEATFSdmg(p1hp,p2dmg,p1def)
                                    if(p2shell2 == "HESH"):
                                        p1hp = shellHESHdmg(p1hp,p2dmg,p1def,fact)
                                if(o5 == "3"):
                                    if(p2shell3 == "AP"):
                                        p1hp = shellAPdmg(p1hp,p2dmg,p1def)
                                    if(p2shell3 == "HE"):
                                        p1hp = shellHEdmg(p1hp,p2dmg,p1def,fact)
                                    if(p2shell3 == "APCR"):
                                        p1hp = shellAPCRdmg(p1hp,p2dmg,p1def)
                                    if(p2shell3 == "HEATFS"):
                                        p1hp = shellHEATFSdmg(p1hp,p2dmg,p1def)
                                    if(p2shell3 == "HESH"):
                                        p1hp = shellHESHdmg(p1hp,p2dmg,p1def,fact)
                                if(o5 == "4"):
                                    if(p2shell4 == "AP"):
                                        p1hp = shellAPdmg(p1hp,p2dmg,p1def)
                                    if(p2shell4 == "HE"):
                                        p1hp = shellHEdmg(p1hp,p2dmg,p1def,fact)
                                    if(p2shell4 == "APCR"):
                                        p1hp = shellAPCRdmg(p1hp,p2dmg,p1def)
                                    if(p2shell4 == "HEATFS"):
                                        p1hp = shellHEATFSdmg(p1hp,p2dmg,p1def)
                                    if(p2shell4 == "HESH"):
                                        p1hp = shellHESHdmg(p1hp,p2dmg,p1def,fact)
                        
                    if(a == "t"):
                        if(gracz == 1):
                            p1t = 2
                        if(gracz == -1):
                            p2t = 2

                gracz *= -1

            else:
                if(p1hp == 0):
                    print("Player 2 wins!")
                elif(p2hp == 0):
                    print("Player 1 wins!")

            