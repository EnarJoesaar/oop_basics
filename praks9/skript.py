#vajalike klasside importimine
from praks9.dok import Tuba, AknadUksed
#ruumi mõõtude küsimine ja sisestamine
print("Ruumi moodud: ")
p = float(input("pikkus: "))
l = float(input("laius: "))
k = float(input("kõrgus: "))
#toa loomine
tuba = Tuba(p, l, k)
#vajadusel akende ja uste lisamine
vastus = (input("Kas aknaid või uksi on? :"))
while vastus == "jah":
    l = float(input("Mis on akna või ukse laius: "))
    k = float(input("Mis on akna või ukse kõrgus: "))
    aken_uks = AknadUksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas aknad või uksed on olemas: ")
#tapeedi rulli mõõtmete sisestamine
print("Tapeedi rulli suurust on vaja ")
tp = float(input("Tapeedi rulli pikkus: "))
tl = float(input("Tapeedi rulli laius: "))
#vastuse väljastamine
print("Tapeete on vaja kleepida: " + str(tuba.toopind()) + " ruutmeetrites")
print("Tapeedi rulle on vaja: " + str(tuba.tapeet(tp, tl)))