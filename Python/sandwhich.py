def sandwichOption():
    sandwich = ["Turkey", "Chicken", "Ham"]
    for x in sandwich:
        print(x)

def cerealOption():
    cereal = ["Frosted Flakes", "Captain Crunch", "Trix", "Pops"]
    for y in cereal:
        print(y)

print("Lets get something to eat!")
motivation = input("Sandwhich or Cereal: ")

if motivation == "Sandwhich":
    sandwichOption()
    sandwich = input("Make a Choice: ")
    print("You've choosen to make a " + sandwich + " sandwich")

elif motivation == "Cereal":
    cerealOption()
    cereal = input("Make a Choice: ")
    print("You've choosen to make a " + cereal)
else:
    print("If you dont choose, you starve!")