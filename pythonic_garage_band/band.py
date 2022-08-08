class Band():
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for players in self.members:
            solos.append(players.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician():

class Guitarist(Musician):

class Bassist(Musician):

class Drummer(Musician):
