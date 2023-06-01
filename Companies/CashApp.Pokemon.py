from enum import Enum


class DamageType(Enum):
    BLUNT = 1
    CUT = 2
    SPIRIT = 3
    FIRE = 4
    ICE = 5


class RACE(Enum):
    DRAGON = 1
    BEAST = 2
    GHOST = 3


class PokemonBase(object):
    def __init__(self, stat, indiv_values, type=TypeEnum.NORMAL, name='???', level=1):
        self.level = level

        self.skills = []
        self._type = None
        self._name = ''
        self._hp = 1
        self._attack = 1
        self._defense = 1

        self._type = type
        self._name = name
        self.ResetStat()
        self.Grow(level)

    def attack(self):
        return (self._attack, self._type)

    def defend(self, attack, type):
        dmg = 0
        self._hp -= dmg
        if self._hp <= 0:
            print("defeated")

    def ResetStat(self):

    def Grow(self, level):
        '''
            level up and increase stat of pokemon
        '''
        if level < self.level:
            raise PokemonPKError()
        else:
            self.level = level
            origin_HP = self._hp
            self._hp = int((self._stat.hp + self._indiv_values.hp) * self.level / 50 + 10 + self.level)
            self._attack = int((self._stat.attack + self._indiv_values.attack) * self.level / 50 + 5)
            self._defense = int((self._stat.defense + self._indiv_values.defense) * self.level / 50 + 5)
            self._special_attack = int(
                (self._stat.special_attack + self._indiv_values.special) * self.level / 50 + 5)
            self._special_defense = int(
                (self._stat.special_defense + self._indiv_values.special) * self.level / 50 + 5)
            self._speed = int((self._stat.speed + self._indiv_values.speed) * self.level / 50 + 5)
            if self.hp != 0:
                self.hp = (self._hp - origin_HP) + self.hp

class Charizard(PokemonBase):
    def __init__(self):
        name='喷火龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.FIRE+TypeEnum.FLYING,name=name)

# class Pokemon:
#     def __init__(self, hp=100):
#         self.hp = hp
#
#
# def battle(p1, p2):
#     p1.hp = 20
#     p2.hp = 30
#     print('haha')
#
#
# def arena(team1, team2):
#     print('wins')
#
#
# p1 = Pokemon()
# p2 = Pokemon(25)
# #
# battle(p1, p2)
# print(p1.hp,' ',p2.hp)
