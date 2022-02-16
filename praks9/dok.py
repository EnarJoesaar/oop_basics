class AknadUksed:
    """
    Klaas akna või ukse objekti kirjeldamiseks
    """
    def __init__(self, laius, korgus):
        """
        Akna või ukse objekti loomiseks vajalik konstruktor Aken või uks määratakse pindalaga tema mõõtudest lähtuvalt
        """
        self.pindala = laius * korgus
class Tuba:
    """
    Tuba klass.
    """
    def __init__(self, p, l, k):
        """
        Konstruktor võtab pikkuse, laiuse ja kõrguse ning eraldi aknad_uksed
        """
        self.pikkus = p
        self.laius = l
        self.korgus = k
        self.aknad_uksed = []
    def lisaAkenUks(self, laius, korgus):
        """
        Lisab akna või ukse
        """
        self.aknad_uksed.append(AknadUksed(laius, korgus))
    def fullala(self):
        """
        Arvutab toa pindala
        """
        return 2 + self.korgus * (self.pikkus + self.laius)
    def toopind(self):
        """
        liidab toa pindala ja akna või ukse pindala
        """
        uus_pindala = self.fullala()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala + element.pindala
        return uus_pindala
    def tapeet(self, tp, tl):
        """Arvutab mitu tapeedi rulli on vaja"""
        return int(self.toopind() / (tp * tl)) + 1