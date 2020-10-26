print("""Let's create a story!
We're going to the supermarket. 
The door to go outside our apartment is in front of us. 
Do we leave or stay?
""")

door = input("> ")
door = door.lower()

if door == "stay":
    print("Let's just stay at home today.")
    print("What do you want to do at home?")

    activity = input("> ")
    activity = activity.lower()

    if activity == "watch tv":
        print("After a couple minutes of watching tv, you fall asleep never to wake again.")
    else:
        print("""Who wants to do that?
        The building explodes from a natural gas leak.""")

elif door == "leave":
    print("Let's go out!")
    print("Should we take the stairs or the elevator?")

    direction = input("> ")
    direction = direction.lower()
    
    if direction == "elevator":
        print("""
        You press the button for the elevator.
        The elevator opens and a tiger jumps out an mauls you to death!
        Who would have thought that would have happened?""")
    else:
        print("""Let's get some exercise in!
        You take the stairs down.
        You go down the first step, and stumble down!
        You roll down 3 flights of stairs and finally stop.
        You've broken all the bones in your body. 
        There's no way you can survive that, you're dead.""")
else:
    print("""Hmmmm, what do you want to do again? 
    Stay or leave?
    It's not like anything bad will happen....""")