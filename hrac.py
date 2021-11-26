import random

def hodkostkou(strany=6):
    return random.randint(1, strany)

class Hrac:

    def __init__(self, profese, ziskanasila, ziskanemagy):
        self.profese = profese
        if profese == "Hranicar*ka":
            startsila = 5
            startmagy = 2
        elif profese == "Zaklinac*ka":
            startsila = 4
            startmagy = 4
        elif profese == "Druid*ka":
            startsila = 3
            startmagy = 6
        elif profese == "Zoldak*cka":
            startsila = 4
            startmagy = 4
        elif profese == "Mnich*Jeptiska":
            startsila = 3
            startmagy = 6
        else:
           
        self.ubranezivoty = 0
        self.vycerpanemagy = 0
        self.zkusenost = 3
        self.zlataky = 3
        self.maxzivoty = startsila + ziskanasila
        self.zivoty = startsila + ziskanasila - self.ubranezivoty
        self.sila = self.zivoty
        self.maxvule = startmagy + ziskanemagy
        self.vule = startmagy + ziskanemagy - self.vycerpanemagy
        self.zivy = True

        def predstav_se(self):
           return f"Jsem {self.profese}, mam {self.startsila} zivotu a {self.startvule} magu"
   

