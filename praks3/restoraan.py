class Restoraan():
    def __init__(self, restoraani_nimi,  soogi_tyyp):
        self.restoraani_nimi = restoraani_nimi
        self.soogi_tyyp = soogi_tyyp
    def info(self):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))

    def kirjelda_restoran(self):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))


    def ava_restoran(self):
        print("Restoraan on avatud")

