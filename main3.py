import random

def rollDice():
    return random.randint(1,6)

#result = rollDice()
#print(f"The dice rolled: {result}")


class unit:
    def __init__(self, health, hit):
        self.health = health
        self.hit = hit

goblin = unit(10, 2)
man = unit (10, 3)

print(f"Man's health is {man.health}")

print("If the dice rolls above a 3, the goblin successfully attacks the man")
result = rollDice()
print(f"The dice rolled: {result}")
if result > 3:
    print("The goblin attacks the man")
    man.health -= goblin.hit
else:
    print("The goblin misses!")

print(f"The man's health is now {man.health}")