# 11
class BankAccount:
    def __init__(self, b):
        self.balance = b

    def check_balance(self):
        if self.balance == 0:
            print("Hisob bosh")
        else:
            print("Balans: 1000$")


b1 = BankAccount("")
b1.check_balance()

# 12
class Light:
    def __init__(self, s):
        self.state = s

    def status(self):
        if self.state == self.state:
            print("chiroq yoniq")
        else:
            print("Chiroq ochiq")

l1 = Light(True)
l1.status()

# 13
class Door:
    def __init__(self, i):
        self.is_open = i

    def check(self):
        if self.is_open != self.is_open:
            print("Eshik ochiq")
        else:
            print("Eshik yopiq")

d1 = Door(False)
d1.check()

# 14
class GamePlayer:
    def __init__(self, n, s):
        self.name = n
        self.score = s

    def result(self):
        if self.score > 50:
            print(f"{self.name} yutdi")
        else:
            print(f"{self.name} yutqazdi")

g1 = GamePlayer("Ali", 55)
g1.result()

# 15
class Temperature:
    def __init__(self, d):
        self.degree = d

    def check_weather(self):
        if self.degree > 25:
            print("Issiq")
        else:
            print("Sovuq")

t1 = Temperature(23)
t1.check_weather()

# 17
class Speed:
    def __init__(self, s):
        self.speed = s

    def chech(self):
        if self.speed > 100:
            print("Tezlik oshdi")
        else:
            print("Normal")

s1 = Speed(120)
s1.chech()

# 18
class AgeCheck:
    def __init__(self, a):
        self.age = a

    def is_adult(self):
        if self.age >= 18:
            print("Voyaga yetgan")
        else:
            print("Voyaga yetmagan")

a1 = AgeCheck(20)
a1.is_adult()

# 19
class Internet:
    def __init__(self, is_connected):
        self.is_connected = is_connected

    def status(self):
        if self.is_connected:
            print("Internet bor")
        else:
            print("Internet yo'q")


i1 = Internet(True)
i1.status()

i2 = Internet(False)
i2.status()

# 20
class Battery:
    def __init__(self, percent):
        self.percent = percent

    def status(self):
        if self.percent < 20:
            print("Quvvat kam")
        else:
            print("Yaxshi")


b1 = Battery(15)
b1.status()

b2 = Battery(45)
b2.status()
