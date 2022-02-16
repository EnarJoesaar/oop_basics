class AknadUksed:
    def __init__(self, laius, korgus):
        self.pindala = laius * korgus
class Tuba:
    def __init__(self, p, l, k):
        self.pikkus = p
        self.laius = l
        self.korgus = k
        self.aknad_uksed = []
    def lisaAkenUks(self, laius, korgus):
        self.aknad_uksed.append(AknadUksed(laius, korgus))
    def fullala(self):
        return 2 + self.korgus * (self.pikkus + self.laius)
    def toopind(self):
        uus_pindala = self.fullala()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala + element.pindala
        return uus_pindala
    def tapeet(self, tp, tl):
        return int(self.toopind() / (tp * tl)) + 1

print("Ruumi moodud: ")
p = float(input("pikkus: "))
l = float(input("laius: "))
k = float(input("kõrgus: "))

tuba = Tuba(p, l, k)

vastus = (input("Kas aknaid või uksi on? :"))
while vastus == "jah":
    l = float(input("Mis on akna või ukse laius: "))
    k = float(input("Mis on akna või ukse kõrgus: "))
    aken_uks = AknadUksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas aknad või uksed on olemas: ")

print("Tapeedi rulli suurust on vaja ")
tp = float(input("Tapeedi rulli pikkus: "))
tl = float(input("Tapeedi rulli laius: "))

print("Tapeete on vaja kleepida: " + str(tuba.toopind()) + " ruutmeetrites")
print("Tapeedi rulle on vaja: " + str(tuba.tapeet(tp, tl)))









