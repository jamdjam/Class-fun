import os
from huntable_camps import wolfEasy
from map import Map


class eve:
    def __init__(self, name):
#--------------------------------------------------------Class stats and name----------------------------------------------------------------------#
        self.name = name
        self.lvl = 5

        self.hp = 465 #health points
        self.maxHP = 465 #Max health current health can not surpass
        self.mana = 350
        self.maxMana = 350 #Max mana current mana can not surpass
        self.ad = 50 #attack damage
        self.ap = 50 #ability power
        self.arm = 34 #armour
        self.mr = 32 #Magic Resist

        self.gold = 400

        self.xp = 0 #Current xp
        self.xpCap = 100 #XP until next level

        self.Attacks = [{"Name": "Scratch", "movID": 1, "Dmg": 0.8, "Type": "AD"},
                        {"Name": "Shriek", "movID": 2, "Dmg": 0.7, "Type": "AP"}] 
        
        self.Consumables = [{"Name": "Health Potion", "Value": 150, "Qty": 3,"Dsc": "Restores 150 points of health", "ID": 1}]

        self.Items = []

    def attacksReturn(self):
        return self.Attacks


#------------------------------------------------------Using Consumables and Such----------------------------------------------------------#
 
    def Applicables(self):
        os.system("cls")
        for item in self.Consumables:
            print("{}: {}. Quantity: {} | {} ".format(str(item["ID"]), item["Name"], str(item["Qty"]), item["Dsc"]))

        x = input("Selection: ")
        for item in self.Consumables:
            if str(item["ID"]) == x:
                if self.hp >= self.maxHP:
                    input("Health is already max! ")
                    break
                elif item["Qty"] <= 0:
                    input("You have no {}s left! ")
                    break
                else:
                    self.hp += item["Value"]
                    if self.hp > self.maxHP:
                        print("Hello there")
                        self.hp += (self.maxHP - self.hp)
                    item["Qty"] -= 1 
                    input("{}'s HP has been increased to {}/{}! ".format(self.name, str(self.hp), str(self.maxHP)))
            



    def printStats(self):

        print("Name: {} || Level: {} || XP: {}\nHP: {}/{} || Mana: {}/{} || AD: {} || AP: {} || Armour: {} || Magic Resist: {} "
        .format(self.name, self.lvl, self.xpBar(self.xp, self.xpCap), self.hp, self.maxHP, self.mana,self.maxMana, self.ad, self.ap, self.arm, self.mr))
        #print(self.xp, self.xpCap) #testing
        #self.xpBar(self.xp, self.xpCap)

    def xpBar(self, curXP, maxXP): #reference to math used here https://appdividend.com/2022/06/23/how-to-calculate-a-percentage-in-python/
        #using the percentage of the xp (rounded to the nearest 10) to convert it into a bar. 1 block representing 10% of the xp bar example 30% bar: ∎∎∎□□□□□□□
        quotient = curXP / maxXP
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

#-------------------------------------------------------------Stats per level-up---------------------------------------------------------------#
    def levelUp(self):
        hpPerLvl = 32
        manaPerLvl = 29
        adPerLvl = 12
        apPerLvl = 11
        armPerLvl = 11
        mrPerLvl = 11

        self.lvl += 1
        self.hp += hpPerLvl
        self.maxHP += hpPerLvl
        self.mana += manaPerLvl
        self.maxMana += manaPerLvl
        self.ad += adPerLvl
        self.ap += apPerLvl
        self.arm += armPerLvl
        self.mr += mrPerLvl

        self.xpCap = self.xpCap * 1.4 
        return(self.lvl)

    def xpCheck(self):
        level = None
        #While eve is past the xp cap increase level and minus the XPcap from current XP 
        while self.xp > self.xpCap:
            os.system("cls")
            self.xp = self.xp - self.xpCap
            level = self.levelUp()
            input("{} has reached level {}!\nPress enter to continue ".format(self.name, self.lvl))
        return(level)

#-----------------------------------------------------Armour and Magic resist Multipliers!-----------------------------------------------------#

#https://www.strategyzero.com/blog/2011/league-of-legends-armour-and-magic-resistance-damage-reduction/#:~:text=Taking%20the%20damage%20multiplier%20(DM,of%20damage%20that%20is%20reduced.
#^^ very important in damage and armour determination
    def damage_multipler_AD(self):
        if self.arm >= 0:
            multipler = 100/(100+self.arm) #I would sum this up in a comment, however
        else:                               #Because i dropped out of uni I am unable too.
            multipler = 2 - (100/(100-self.arm)) #got it working first try though. take a look at this link instead! https://wikimedia.org/api/rest_v1/media/math/render/png/49de2870780ad3077293edbfabdf45b8afed4509
        return (multipler)

    def damage_multiplier_AP(self):
        if self.mr >= 0:
            multipler = 100/(100+self.mr)
        else:
            multipler = 2 - (100/(100-self.mr))
        return (multipler)
    
    def StatApp(self):
        for item in self.Items:
            if item["applied"] == "no":
                for stat in item["stats"]:
                    if stat == "ap":
                        self.ap += item["stats"]["ap"]
                        item["applied"] = "yes"
                    elif stat == "ad":
                        self.ad += item["stats"]["ad"]
                        item["applied"] = "yes"
                    elif stat == "hp":
                        self.hp += item["stats"]["hp"]
                        item["applied"] = "yes"
                    elif stat == "arm":
                        self.arm += item["stats"]["arm"]
                        item["applied"] = "yes"
                    elif stat == "mr":
                        self.mr += item["stats"]["mr"]
                        item["applied"] = "yes"



    
    def xp150(self): #testing only
        self.xp += 140
        self.xpCheck()

#----------------------------------------------------- END OF CLASS -------------------------------------------------------------



class shop:
    def __init__(self):
        self.items = [{"ID" : 1, "name" : "Enchanted Note", "cost" : 300, "stats" :  {"ap" : 25, "hp" : 40}, "sell" : 175, "applied" : "no"},
                    {"ID" : 2, "name" : "Warped Jade Stone" , "cost" : 450, "stats" : {"arm" : 15, "mr" : 15}, "sell" : 200, "applied" : "no"},
                    {"ID" : 3, "name" : "Splintered Club" , "cost" : 350, "stats" : {"ad" : 20, "hp" : 50}, "sell" : 185, "applied" : "no"},
                    {"ID" : 4, "name" : "Eyed Pendant" , "cost" : 1100, "stats" : {"ap" : 45, "mr" : 15, "ad": 20}, "sell" : 200, "applied" : "no"}]

        self.consumables = [{"ID" : 1, "name": "Health Potion", "cost" : 75}]

        
    def shopChoice(self):
        os.system("cls")
        print("1. Consumables    |    2.Items \n")
        x = input()
        if x == "1":
            self.cons()
        elif x == "2":
            self.item()

    
    def cons(self):
        g = b1.gold
        os.system("cls")
        print("Gold: {}".format(str(g)))
        #print(self.consumables)

        for item in self.consumables:
            print("{}.{} (Cost : {})".format(str(item["ID"]), item["name"], item["cost"]))
        x = input("\n \nPlease select an item you would like to purchase! (Enter e to exit :D)")
        for item in self.consumables:
            if str(item["ID"]) == x:
                for list in b1.Consumables:
                    if list ["ID"] == item["ID"]:
                        if g - item["cost"] < 0:
                            input("You do not have enough gold! ")
                            break
                        list["Qty"] += 1
                        b1.gold -= item["cost"]

    def item(self):
        g = b1.gold
        os.system("cls")
        print ("Gold: {}".format(g))

        for item in self.items:
            print("{}. {} (Cost : {})  || Stats: {}".format(str(item["ID"]), item["name"], item["cost"], item["stats"]))
        x = input("\nPlease select an item you would like to purchase! ")
        ind = 0
        for item in self.items:
            if g >= item["cost"]:
                if str(item["ID"]) == x:
                    b1.Items.append(item)
                    b1.gold -= item["cost"]
                    self.items.pop(ind)
            ind += 1


        b1.StatApp()

b1 = eve("Sarala")
store = shop()
explore = Map()

def fight():
    while b1.hp > 0 and enemy.hp > 0:
        os.system("cls")
        enemy.printStats()
        b1.printStats()
        moves = b1.attacksReturn()
        
        movIDs = []

        for move in moves: #Shows the player their selection of moves 
            print(str(move["movID"]), move["Name"])
            movIDs.append(move["movID"])
            print("Damage: {} / {}".format(move["Dmg"], move["Type"]))

        i = None
        while i not in movIDs:
            x = input("please select a move! ")
            if x.isdigit():
                i = int(x) #comment
            else: print("Please input a move Number")

        for move in moves: #goes through moves in characters dicttionary to find one selected by the user
            if i == move["movID"]:
                if move["Type"] == "AD":
                    dmgNum = (move["Dmg"] * b1.ad)
                    multiplier = enemy.damage_multiplier_AD() #NEED TO TEST IF THESE ARE ACTUALLY WORKING, I cant be bothered atm
                elif move["Type"] == "AP":
                    dmgNum = (move["Dmg"] * b1.ap)
                    multiplier = enemy.damage_multiplier_AP()
                input("{} has used {} and dealt {} Damage! ".format(b1.name, move["Name"], round(dmgNum * multiplier)))
                enemy.hp -= round(dmgNum * multiplier)

        if enemy.hp <= 0:
            b1.xp += enemy.xpReturn
            b1.gold += enemy.goldReturn
            os.system("cls")
            input("Congratulations, {} has beat {}! {} has received {} gold and {}XP!\nPress enter to continue ".format(b1.name, enemy.name, b1.name, enemy.goldReturn, enemy.xpReturn))
            b1.xpCheck()
            break
 
        #enemy move

        enMoves = enemy.attacksReturn()
        x = 1
        for enMove in enMoves:
            if x == enMove["movID"]:
                if enMove["Type"] == "AD":
                    dmgNum = (enMove["Dmg"] * enemy.ad)
                    multiplier = b1.damage_multipler_AD()
                elif move["Type"] == "AP":
                    dmgNum = (enMove["Dmg"] * enemy.ap)
                    multiplier = b1.damage_multiplier_AP()
                damage = round(dmgNum * multiplier)
                input("{} has used {} and dealt {} Damage! ".format(enemy.name, enMove["Name"], str(damage)))
                b1.hp -= damage

        if b1.hp < 0:
            input("You must return and heal!\nPress enter to continue!")


while __name__ == "__main__":
    os.system("cls")
    b1.printStats()

    choice = str(input("1. Fight  ||  2. Consumables  ||  3.market\n"))
    if choice == "1":
        enemy = wolfEasy()
        enemy.perLvl()
        fight()
    elif choice == "2":
        b1.Applicables()
    elif choice == "3":
        store.shopChoice()
    elif choice == "4":
        explore.lvlCheck(b1.lvl)
        explore.areaP()


