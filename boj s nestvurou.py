from hrac import *
from nestvura import *

def bojsnestvurou (co, koho):
    print(koho.profese + " narazil*a na nestvuru. Vypada jako " + co.jmeno +"! Nema na vybranou, jde se bojovat.")
    bylsoubojvuli = False
    while co.zivy == True and koho.zivy == True:
            if co.sila < 0 and ((koho.vule - 2) - co.vule)<=(koho.sila - co.sila):
                if (koho.sila + (hodkostkou())) > (co.sila + (hodkostkou())):
                    co.zivoty = co.zivoty -1
                    if co.zivoty == 0:
                        print(f"{koho.profese} zabil*a nestvuru známou jako {co.jmeno} a ziskal*a {co.zkusenost} bodu zkusenoti.")
                    else:
                        print("Jeden zivot dole, jen tak dal!")
                elif (koho.sila + (hodkostkou())) == (co.sila + (hodkostkou())):
                    print("Je to remiza!")
                    break
                elif (koho.sila + (hodkostkou())) < (co.sila + (hodkostkou())):
                    print("Nestvura vyhrala. " + koho.profese + "ztraci jeden zivot.")
                    koho.ubranezivoty = koho.ubranezivoty +1
                    if koho.zivoty == 0:
                        print(self.profese + " precenil*a sve sily. Budeme na tebe vzpominat.")
                        koho.zivy = False
                        break
