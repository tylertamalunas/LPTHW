from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # opens file in write mode

print("Truncating the file. Goodbye!")
#target.truncate() # erases the contents of the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write theese to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n") # writes the lines into the file

print("And finally, we close it.")
target.close() # closes and saves the file. 