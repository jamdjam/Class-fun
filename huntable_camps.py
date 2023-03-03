import random

class wolf:
    def __init__(self, plyrLvl):

        self.lvl = random.randrange(1, 4)

        self.name = "Bella Wolf"
        self.maxHP = 228 #max health used to print health bar
        self.hp = 228 #health points
        self.ad = 18 #attack damage
        self.ap = 9 #ability power
        self.arm = 21 #armour
        self.mr = 21 #Magic Resist

        self.xpReturn = 65 #XP returned to the player character
        self.goldReturn = 30 #gold returned to the player

        self.Attacks = [{"movID" : 1, "Name" : "Gash", "Dmg" : 0.9, "Type" : "AD"}]

    def attacksReturn(self):
        return(self.Attacks)


         
    def HPBar(self, curHP, maxHP): #reference to math used here https://appdividend.com/2022/06/23/how-to-calculate-a-percentage-in-python/
        #using the percentage of the xp (rounded to the nearest 10) to convert it into a bar. 1 block representing 10% of the xp bar example 30% bar: ∎∎∎□□□□□□□
        quotient = curHP / maxHP
        percent = round(quotient * 100, -1)
        #print(percent)
        display = ""
        for i in range(0, 10, 1):
            if percent > 0:
                display += "∎"
                percent -= 10
            else:
                display += "□"
 
        return(display)
    
    def printStats(self):
         print("Name: {} || Level: {} ||\nHP: {} || AD: {} || AP: {} || Armour: {} || Magic Resist: {} "
        .format(self.name, self.lvl, self.HPBar(self.hp, self.maxHP), self.ad, self.ap, self.arm, self.mr))

    def perLvl(self):
        hpPerLvl = 32

        adPerLvl = 9
        apPerLvl = 8
        armPerLvl = 7
        mrPerLvl = 6
        xpPerLvl = 16
        goldPerLvl = 15



        for i in range(1, self.lvl, 1):
            self.maxHP += hpPerLvl
            self.hp += hpPerLvl
            self.ad += adPerLvl
            self.ap += apPerLvl
            self.arm += armPerLvl
            self.mr += mrPerLvl

            self.goldReturn += goldPerLvl
            self.xpReturn += xpPerLvl

    def damage_multiplier_AD(self):
        if self.arm >= 0:
            multipler = 100/(100+self.arm)
        else:
            multipler = 2 - (100/(100-self.arm))
        return (multipler)

    def damage_multiplier_AP(self):
        if self.mr >= 0:
            multipler = 100/(100+self.mr)
        else:
            multipler = 2 - (100/(100-self.mr))
        return (multipler)
