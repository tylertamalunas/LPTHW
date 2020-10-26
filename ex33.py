x = input("What's your number: ")

def tyler(x):

    i = 0
    numbers = []

    while i < int(x):
        print(f"At the top is {i}")
        numbers.append(i)

        z = int(input("Increase i by: "))
        i += z
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

tyler(x)