name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Choose which way you wanna go: ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. Type 'walk' to walk or 'swim' to swim accross: ").lower()

    if answer == "swim":
        print("You swam accross and eaten by a alligotor!")
    elif answer == "walk":
        print("You walked for many miles and ran out of water and you died!")
    else:
        print("You stayed there and Died!")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly,  do you want to cross it or head back? (cross/back): ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to him?(yes/no): ").lower()

        if answer == "yes":
            print("You talked to the stranger and wow, he is now your crime partner. You Won the game!")
        elif answer == "no":
            print("You didn't talked to the stranger and the stranger killed you!")
        else:
            print("The stranger killed you!")

    elif answer == "back":
        print("You go back and died!")
    else:
        print("You stayed there and Died!")
else:
    print("You stayed there and Died!")

print("Thank You", name, "for playing!")