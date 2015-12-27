class Enemy:
    life = 3

    def attack(self):
        print('ouch'
              '   /^\/^\   '
              ''
              ''
              '')
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print('I am dead supah')

        else:
            print(str(self.life) + ' life left supah')

enemy1 = Enemy()
e1 = enemy1.attack()
