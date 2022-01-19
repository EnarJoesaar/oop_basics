class Restoraan():
    def __init__(self, restoraani_nimi,  soogi_tyyp, teenindatud_kylastajad):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp
        self.teenindatud_kylastajad = teenindatud_kylastajad
    def info(self):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))

    def kirjelda_restoran(self):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))


    def ava_restoran(self):
        print("Restoraan on avatud")

    def maara_teenindatud_kylalised(self):
        esimene = input("Sisesta mitu külalist on teenindatud: " + str(self.teenindatud_kylastajad)9,9)
        print(str(self.teenindatud_kylastajad))

    def suurenda_teenindatud_kylalised(self):
        teine = input("Sisesta mitu külalist on veel teenindatud: " + str(self.teenindatud_kylastajad))
        print(str(self.teenindatud_kylastajad))
