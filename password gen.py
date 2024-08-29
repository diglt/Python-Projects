import random

password = []
characters = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
strpassword = ""

def ReturnRandomInt():
    return random.randint(0, 9)

def GeneratePassword(uppercase, numbers, character):
    global strpassword
    
    for i in range(5):
        if uppercase:
            letter = random.choice(alphabet).upper()
            password.append(letter)
        else:
            letter = random.choice(alphabet)
            password.append(letter)

    for a in range(5):
        if numbers:
            number = ReturnRandomInt()
            password.append(str(number))
        if character:
            char = random.choice(characters)
            password.append(char)
    
    random.shuffle(password)
    
    for c in range(len(password) - 1):
        strpassword = strpassword + password[c]


upper_case = str(input("Include uppercase letters?: ")).lower()
include_number = str(input("Include numbers?: ")).lower()
include_characters = str(input("Include special characters?: "))

if upper_case[0] == "y":
    upper_case = True
else:
    upper_case = False

if include_characters[0] == "y":
    include_characters = True
else:
    include_characters = False

if include_number[0] == "y":
    include_number = True
    characters.extend("!£$%^&*()")
else:
    include_number = False

GeneratePassword(upper_case, include_number, include_characters)
print(strpassword)
