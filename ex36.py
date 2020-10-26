from sys import exit
from random import randint

has_axe = False
gnoll_dead = False
goblin_dead = False
troll_dead = False
bandit_dead = False

def gnoll_room():
    print("Soon after walking into the room, a gnoll jumps at you from the corner!")
    print("Do you attempt to attack it or block the blow?")
    
    global gnoll_dead

    while True:

        if gnoll_dead == True:
            print("You've killed the gnoll that was guarding the room.")
            print("You see another room further down the passageway that has a big chest in it!")
            print("You can't help but walk toward the room with the chest.")
            chest_room()
        else:
            action = input("> ")

            if "block" in action:
                block()
            elif "attack" in action:
                attack()
                gnoll_dead = True
            else:
                dead("You miscalculated and the gnoll stabbed you through the heart!")

def chest_room():
    print("As you approach the room, you keep a keen eye out for any surprises like the last room...")
    print("You make your way into the room and see everything very clearly.")
    print("There are no creatures anywhere in the room, all you see is the chest.")
    print("As you look at the chest you can't help but think to yourself that it might be trapped.")
    print("What do you want to do? Open the chest or leave?")

    global has_axe

    while True:
            
        action = input("> ")
        action = action.lower()

        if "open" in action:
            print("""You decide to take your chances and open the chest. 
Inside the chest you see a gleaming titanium axe!!!
The axe is a thing of beauty made with remarkable craftmanship.
This is the highest quality weapon you have ever seen.
You decide to take the axe and use it as your new weapon. 
            """)
            has_axe = True

        elif "leave" in action:
            print("You decide to go back to the beginning of the dungeon.")
            start()
        else:
            print("I don't know if that's a good idea, you should either open the chest or leave...")


def goblin_room():

    global goblin_dead

    while True:

        if goblin_dead == True:
            print("The goblin is dead. You decide to take a closer look at the shiny object it was crouching over.")
            print("It was a Titanium suit of armor!! And it happens to fit you perfectly!")
            print("You decide to use it and replace the crappy armor you were using.")
            print("You decide to go back to the start since there is nothing else here.")
            start()
        else:
            print("""As you get closer to the end of the passage, you notice a creature in a room crouching over something shiny.
The creature has no idea you are there and seems to be too focused on what is in front of it. 
Are you going to make a surprise attack, or take the cautious route and keep your block up?
    """)
            action = input("> ")
            action = action.lower()

            if "attack" in action:
                print("You decide to attack the goblin, as you creep closer, you lift your weapon above your head and come down it's head.")
                attack()
                goblin_dead = True
            elif "block" in action:
                print("You decide to creep closer to the creature while keeping your block up.")
                print("You stand right behind it, and it still doesn't notice you...I mean it is pretty stupid, so you shrug and attack.")
                attack()
                goblin_dead = True
            else:
                print("It just sits there with its back to you, it has no idea you're there. It's just a stupid goblin...")
                attack()
                goblin_dead = True


def troll_room():
    print("You go down the North passage.")
    print("As you go further along, the smell gets worse and worse until you can't bear it.")
    print("You walk into a large room at the end, and there is a massive Troll in the room!")
    print("It sees you and lets out a massive roar!!!")
    print("With the Troll bearing down on you and limited time to decide, what do you do?")

    action = input("> ")
    action = action.lower()

    if "attack" in action and has_axe == False:
        print("You dodge the trolls swing and see an opening for its neck!")
        print("You swing at its vitals, but the sword doesn't even pierce the skin...")
        dead("The Troll grabs you and squeezes you until all your juices come out.")
    elif "attack" in action and has_axe == True:
        print("You dodge the Troll, and roll behind its foot. ")
        print("You swing the axe at its ankle, and cut it clean off!")
        print("The Troll falls to the ground with a yell of pain.")
        print("You have a clear opening to the back of its neck now")
        print("You swing the axe down and sever the Trolls head from its body!")
        win()
    else:
        dead("You really think theres anywhere left to go? The Troll bites your head off.")


def block():

    block_roll = randint(0,10)

    if block_roll >= 1:
        print("You block the creature's attack and get ready for the next round.")
    else:
        print("You attempt to block the blow, but it was a feint!")
        dead("The creature changes it's attack and stabs you through the stomach.")
        

def attack():
    
    attack_roll = randint(1,10)


    if attack_roll >= 2:
        print("You slash your sword accross the creature's chest and cut deep.")
        print("The creature looks at its chest as blood is pouring out, and it falls to the floor dead.")
    else:
        print("You try to take a massive swing at the creature, but you completely whiff as the creature dodges your attack.")
        dead("The creature takes advantage of the new opening, and stabs you in the back.")


def dead(why):
    print(why, "You're dead now.")
    exit()


def win():
    print("You've killed all the creatures and taken all the loot in the dungeon.")
    print("There is a passage through some vines that leads outside in the troll room.")
    print("You leave the dungeon to go find more riches in the world!")
    exit(0)


def start():
    print("You entered the dungeon to find riches.")
    print("There are 3 passageways in this room. They are North, East, and West.")
    print("Which way do you go?")

    choice = input("> ")
    choice = choice.lower()

    if goblin_dead == True and gnoll_dead == True:
        print("There's only one way left, North.")
        print("You decide to go the only way you havent been")
        troll_room()
    elif choice == "west" and gnoll_dead == False:
        print("You decide to go through the Western passage.")
        gnoll_room()
    elif choice == "west" and gnoll_dead == True:
        print("You already went that way and killed the gnoll.")
        start()
    elif choice == "east" and goblin_dead == False:
        print("You decide to go through the Eastern passage.")
        goblin_room()
    elif choice == "east" and goblin_dead == True:
        print("You already went that way and killed the goblin.")
        start()
    elif choice == "north":
        print("You take the Northern passage.")
        troll_room()
    else:
        print("You have to choose one of the passageways. There's no turning back at this point...")
        start()

start()