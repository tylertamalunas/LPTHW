ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # stuff = split(ten_things) # split ten_things apart at every space

more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff) # remove the last item in the list more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one) # append(stuff, next_one) # append next_one to the end of stuff
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # pop(more_stuff) # remove the last item in more_stuff
print(' '.join(stuff)) # join(stuff, ' ') # join together all items in stuff with a space between them
print('#'.join(stuff[3:5])) # join(stuff[3:5], '#') # join together items 3 and 4 in stuff with a # between them