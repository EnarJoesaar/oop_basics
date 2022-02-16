class Raamat:
    def __init__(self, pealkiri, autor, hind, reiting):
        self.pealkiri = pealkiri
        self.autor = autor
        self.hind = hind
        self.reiting = reiting

class Raamatupood:
    def __init__(self, nimi, reiting):
        self.nimi = nimi
        self.reiting = reiting

    def saan_lisada_raamat(self, Raamat):
        lisamine = str(input("Sisesta raamatu nimi: "))
        if Raamat.pealkiri == lisamine:
            Raamat.pealkiri == False and print("Teie raamatut polnud") and str(input("Sisesta raamatu nimi: "))

    def lisa_raamat(self, Raamat):
        if Raamat.pealkiri == True:
            print("Teie raamat lisati")

    def saan_eemaldada_raamat(self, Raamat):
        eemalda = str(input("Sisesta raamatu nimi: "))
        if Raamat.pealkiri == eemalda:
            Raamat.pealkiri == True and print("Raamat eemaldati")


    def eemalda_raamat(self, Raamat):
        if Raamat.pealkiri == True:
            del Raamat


    def naita_koik_raamatud(self):
        print(Raamat)


    #def naita_raamatud_hinna_jargi(self):



    # def naita_koige_populaarsem_raamat(self)


