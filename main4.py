import tkinter as tk
import random

def rollDice():
    return random.randint(1,6)

def updateConditions():
    label2.config(text=f"Your health is currently: {player.health}\nThe goblin's health is currently {goblin.health}")

def goblinAction():
    result = rollDice()
    if result > 3:
        player.health -= goblin.hit
    label.config(text=f"The goblin rolled a {result}. Your health is now {player.health}")
    updateConditions()

def goblinAttack():
    root.after(3000, goblinAction)

def click():
    result = rollDice()
    hit = "You rolled higher than a 3. You manage to land a hit!"
    miss = "You rolled 3 or lower. You missed!"
    if result > 3:
        goblin.health -= player.hit
        label.config(text=f"You rolled a {result}.\n{hit}\n The goblin's health is now {goblin.health}")
        updateConditions()
    else:
        label.config(text=f"You rolled a {result}.\n{miss}\n The goblin's health is now {goblin.health}")
        updateConditions()
    goblinAttack()

class unit:
    def __init__ (self, health, hit):
        self.health=health
        self.hit=hit

player = unit(10, 2)
goblin = unit(10, 2)

#The first window
root = tk.Tk()
root.title("Test Roll")
root.geometry("500x500")

#The label to display dice roll result
label = tk.Label(root, text="Roll your dice")
label.place(relx=0.5,rely=0.5, anchor="center")

#Label for displaying starting condition
label2 = tk.Label(root, text=f"Your health is currently: {player.health}\nThe goblin's health is currently {goblin.health}")
label2.place(relx=0.5, rely=0.7, anchor="center")

#Button to roll the dice
button = tk.Button(root, text = "roll dice", command = click)
button.pack()




root.mainloop()


