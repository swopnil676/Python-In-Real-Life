import random

name=input("ENTER YOUR NAME :")

vibes=["cool","dev","x_X","girly","soft","pro"]

for i in range(5):
    print(name + random.choice(vibes) + str(random.randint(5, 9)))