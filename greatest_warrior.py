#!usr/bin/python3
# -*- coding: utf-8 -*-


class Warrior:
    rang = [
        "Pushover", "Novice", "Fighter",
        "Warrior", "Veteran", "Sage",
        "Elite", "Conqueror", "Champion",
        "Master", "Greatest", "Invalid level"
    ]

    def __init__(self):
        """initiate our hero"""
        self.level = 1
        self.experience = 100
        self.achievements = []

    def show_hero(self):
        """print all paremetres"""
        discription = (" Level is: " + str(self.level) + "and EXP is: " + str(
            self.experience) + ". Rank is: " + self.rang)
        print(discription)

    def moving(self):
        """move"""
        print("Hero start moving...")

    def rang(self):
        """rang, but doesn't work :("""
        if self.level <= 9:
            self.rang = rang[0]
        elif 10 >= self.level >= 19:
            self.rang = rang[1]
        elif 20 >= self.level >= 29:
            self.rang = rang[2]
        elif 30 >= self.level >= 39:
            self.rang = rang[3]
        elif 40 >= self.level >= 49:
            self.rang = rang[4]
        elif 50 >= self.level >= 59:
            self.rang = rang[5]
        elif 60 >= self.level >= 69:
            self.rang = rang[6]
        elif 70 >= self.level >= 79:
            self.rang = rang[7]
        elif 80 >= self.level >= 89:
            self.rang = rang[8]
        elif self.level == 100:
            self.rang = rang[9]
        else:
            self.rang = rang[10]
        return self.rang

    def fight(self, enemy):
        """fight """
        if self.level > 100 or self.level < 1:
            return "Invalid level"
        elif self.level == enemy:
            self.experience = self.experience + 10
            return "A good fight"
        elif self.level - enemy == 1:
            self.experience = self.experience + 5
            return "A good fight!"
        elif self.level - enemy >= 2:
            return "Easy fight..."
        elif enemy - self.level <= 5:
            self.experience = self.experience + 20 * (self.level - enemy.level) * (self.level - enemy.level)
            return "An intense fight!"
        else:
            # elif enemy - self.level > 5:
            return "You've been defeated..."

    def _add_experience(self, experience):
        """add exp"""
        self.experience = min(10000, self.experience + experience)

    def training(self, session):
        """initiate traning"""
        (description, experience, min_level) = session
        if self.level >= min_level:
            self.achievements.append(description)
            self._add_experience(experience)
            return description
        return "Not strong enough"

if __name__ == '__main__':
    bruce_lee = Warrior()
    print(bruce_lee.level)  # => 1
    print(bruce_lee.experience)  # => 100
    print(bruce_lee.rang)  # => "Pushover"
    print(bruce_lee.achievements)  # => []
    print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
    # => "Defeated Chuck Norris"
    print(bruce_lee.experience)  # => 9100
    print(bruce_lee.level)  # => 91
    # print(bruce_lee.rang)  # => "Master"
    print(bruce_lee.fight(90))  # => "A good fight"
    print(bruce_lee.experience)  # => 9105
    print(bruce_lee.achievements)  # => ["Defeated Chuck Norris"]
