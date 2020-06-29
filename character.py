from random import randint

class Character:
    def __init__(self,name):
        self.name = name
        self.maxHP = 0
        self.hp = 0
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.level = 0
        self.speed = 0
        self.weight = 0
        self.ac = 0
        self.inventory = []
        self.cls = None
        self.race = None
        self.bg = None
        self.proficiencyBonus = 2
        self.proficiencies = {"acrobatics":False,"animal handling":False,"arcana":False,"athletics":False,"deception":False,"history":False,"insight":False,"intimidation":False,"investigation":False,"medicine":False,"nature":False,"perception":False,"performance":False,"persuasion":False,"religion":False,"sleight of hand":False,"stealth":False,"survival":False}

    def getModifier(self,stat):
        if stat == 1:
            return -5
        elif stat <= 3:
            return -4
        elif stat <= 5:
            return -3
        elif stat <= 7:
            return -2
        elif stat <= 9:
            return -1
        elif stat <= 11:
            return 0
        elif stat <= 13:
            return 1
        elif stat <= 15:
            return 2
        elif stat <= 17:
            return 3
        elif stat <= 19:
            return 4
        elif stat <= 21:
            return 5
        elif stat <= 23:
            return 6
        elif stat <= 25:
            return 7
        elif stat <= 27:
            return 8
        elif stat <= 29:
            return 9
        elif stat == 30:
            return 10
        raise ValueError

    def rollDice(self, num, sides, mod, adv=False, disadv=False):
        rolls = []
        for i in range(num):
            rolls.append(randint(1,sides))
        if adv:
            total = sum(rolls) - min(rolls)
            rolls[rolls.index(min(rolls))] = str(mins(rolls)) + "\u0336"
        elif disadv:
            total = sum(rolls) - max(rolls)
            rolls[rolls.index(max(rolls))] = str(max(rolls)) + "\u0336"
        else:
            total = sum(rolls)
        if mod < 0:
            print(rolls, mod)
        else:
            print(f"{rolls} +{mod}")
        total += mod
        print(f"   = {total}")
        return total

    def rollProficiency(self, proficiency):
        strength = ["athletics"]
        dexterity = ["acrobatics","sleight of hand", "stealth"]
        intelligence = ["arcana","history","investigation","nature","religion"]
        wisdom = ["animal handling","insight","medicine","perception","survival"]
        charisma = ["deception","intimidation","performance","persuasion"]
        if proficiency in strength:
            return self.rollDice(1,20,self.getModifier(self.str)+self.proficiencyBonus if self.proficiencies[proficiency] else 0)
        elif proficiency in dexterity:
            return self.rollDice(1,20,self.getModifier(self.dex)+self.proficiencyBonus if self.proficiencies[proficiency] else 0)
        elif proficiency in intelligence:
            return self.rollDice(1,20,self.getModifier(self.int)+self.proficiencyBonus if self.proficiencies[proficiency] else 0)
        elif proficiency in wisdom:
            return self.rollDice(1,20,self.getModifier(self.wis)+self.proficiencyBonus if self.proficiencies[proficiency] else 0)
        elif proficiency in charisma:
            return self.rollDice(1,20,self.getModifier(self.cha)+self.proficiencyBonus if self.proficiencies[proficiency] else 0)
        else:
            raise ValueError

    def __repr__(self):
        return f"{self.name}\n{self.race} {self.cls} {self.level}\n{self.bg}\n\nHP: {self.hp}/{self.maxHP}\n\nStrength: {self.str}\nDexterity: {self.dex}\nConstitution: {self.con}\nIntelligence: {self.int}\nWisdom: {self.wis}\nCharisma: {self.cha}\n\nAC: {self.ac}\nSpeed: {self.speed}ft\n\nInventory: {self.inventory}\nProficiencies: {self.proficiencies}"

g = Character("Garibaldy")
print(g)
