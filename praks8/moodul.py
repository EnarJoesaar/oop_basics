from praks8.kasutaja import Kasutaja

enar = Kasutaja("Enar", "Joesaar", "EJ", "qwerty")

print(enar.tervita_kasutaja())
print(enar.kirjelda_kasutaja())

class Admin(Kasutaja):
    privileegid = []
    def naita_privileegid(self):
        for pv in range(1, len(self.privileegid) +1):
            print("{0}-{1}".format(pv, self.privileegid[pv-1]))

    def maara_privileegid(self):
        print("Lisa varjante: ")
        while(True):
            valik = input("Sisesta: ")
            if(valik == " "):
                break
            self.privileegid.append(valik)



