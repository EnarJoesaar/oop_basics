class Inimene():
    def __init__(self, e_nimi="nimi", p_nimi="perenimi", arv="1"):
        self.eesnimi = e_nimi
        self.perenimi = p_nimi
        self.vallandatud_k = arv

    def tutvusta(self):
        print("Tere, olen " + str(self.eesnimi) + " " + str(self.perenimi) + "!")

    def __del__(self):
        print("Kõike head, " + str(self.eesnimi) + ", " + str(self.perenimi) + "!")

    def vallandatud(self):
        if self.vallandatud_k == 0:
            print(str(self.eesnimi) + " " + str(self.perenimi) + "Oled kahjuks vallandatud!")
