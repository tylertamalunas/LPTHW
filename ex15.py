from sys import argv

script, filename = argv
# Opens the file and saves it to the variable txt
txt = open(filename)

print(f"Here's your file {filename}:")
# calls the read function on txt variable 
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
# opens the file saved to the file_again variable and saves it to txt_again
txt_again = open(file_again)
# calls the read funtion on the txt_again variable
print(txt_again.read())