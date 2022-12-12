class Man():
    def makesound(self):
        print('Имитирует кряканье')

    def clother(self):
        print('Человек в одежде')

class Duck():
    def makesound(self):
        print('Крякает')

    def clother(self):
        print('Утка в шляпе')

person = Man()
animal = Duck()

for smth in(person, animal):
    smth.makesound()
    smth.clother()