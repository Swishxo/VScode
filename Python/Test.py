"""
user = int(input("Choose a player: player1 or player2"))

player1 = 1
player2 = 2

open = True

if (user == player1 or player2) and (open == True):
    print(f"player{user} took the shot")
    open = False
elif (user != player1 or player2) and (open == False):
    print(f"{player1} and {player2} is blocked")
    print("Defense stripped the ball")
else:
    print("Opposing team scored")
"""


sandwich = ["Turkey", "Chicken", "Ham"]
drinks = ["Soda", "Water", "Juice"]
kitchen = ["Cereal"]

combo = sandwich + drinks
kitchen.append(sandwich)

print("Lets get something to eat!")

motivation = input("Want to make a Sandwich! (True or False): ")

print(motivation + " <----1")
if motivation:
    print("Works")