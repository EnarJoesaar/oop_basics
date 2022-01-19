class inimene():

    jk = 0

    def __init__(self):
        self.id = inimene.jk + 1
        inimene.jk += 1

    def info(self):
        print("id = {0}".format(self.id))