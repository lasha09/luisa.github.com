#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
in_dictionary = False


print("Can your password survive a dictionary attack?")

code = input("Type in a trial password: ")

for line in f:
    if line.strip() == code.strip():
        in_dictionary = True
        print("ERROR! YOUR PRIVACY IS IN DANGER,,you found the word! try again! ", line.strip())
        break

if not in_dictionary:
        print("HOORAH YOU HAVE A GOOD PASSWORD")
        


#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords


#Write logic to see if the password is in the dictionary file below here:
