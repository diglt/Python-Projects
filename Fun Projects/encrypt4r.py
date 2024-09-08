# ok yes, i know i normally do modules for my more recent projects. However, it's alot less hassle to spread this script if all the libraries and functions are already preinstalled in python
# so yes ok good i do stuf ahkdwlaldlasldl

title = """                                                                                                    
\x1b[31m                                                                                         ,d8                
                                                                            ,d         ,d888                
                                                                            88       ,d8" 88                
 ,adPPYba,  8b,dPPYba,    ,adPPYba,  8b       d8  8b,dPPYba,  8b,dPPYba,  MM88MMM  ,d8"   88    8b,dPPYba,  
a8P_____88  88P'   `"8a  a8"     ""  `8b     d8'  88P'   "Y8  88P'    "8a   88   ,d8"     88    88P'   "Y8  
8PP"""""""  88       88  8b           `8b   d8'   88          88       d8   88   8888888888888  88          
"8b,   ,aa  88       88  "8a,   ,aa    `8b,d8'    88          88b,   ,a8"   88,           88    88          
 `"Ybbd8"'  88       88   `"Ybbd8"'      Y88'     88          88`YbbdP"'    "Y888         88    88          
                                         d8'                  88                                            
                                        d8'                   88                                            
"""

import base64
import random


Methods = ["Caesar Cipher (Only Takes Characters)", "Base 64 (Takes both Characters, Numbers and Special Characters)"]
Choices = ["Encryption", "Decryption"]
Characters = []
Numbers = []
Special_Characters = []

Encoded_Table = []
Decoded_Table = []

Characters.extend("abcdefghijklmnopqrstuvwxyz")
Numbers.extend("0123456789")

Continue_Running = True
My_Method = None
My_Choice = None
User_String = None


def AddToString(letter, choice, shift_number):
    if choice:
        new_index = Characters.index(letter) + shift_number

        if new_index > len(Characters) - 1:
            new_index = new_index - len(Characters)
            new_letter = Characters[new_index]

            Encoded_Table.append(new_letter)
        else:
            Encoded_Table.append(Characters[new_index])

    else:
        new_index = Characters.index(letter.lower()) + shift_number

        if new_index > len(Characters) - 1:
            new_index = new_index - len(Characters)
            new_letter = Characters[new_index].upper()

            Encoded_Table.append(new_letter)
        else:
            Encoded_Table.append(Characters[new_index].upper())



def ReverseLetters(letter, shift_number, choice):
    if choice:
        new_index = Characters.index(letter) - shift_number

        if new_index < 0:
            new_index += len(Characters)

        Decoded_Table.append(Characters[new_index])
    else:
        new_index = Characters.index(letter.lower()) - shift_number

        if new_index < 0:
            new_index += len(Characters)

        new_letter = Characters[new_index].upper()

        Decoded_Table.append(new_letter)


# Some functions to include numbers, possibly add to ceaser in future updates.

#def AddToStringNumbers(letter, shift):
#    new_index = Numbers.index(letter) + shift
#
#    while new_index > len(Numbers):
#        new_index = new_index - len(Numbers)
#
#    if new_index < len(Numbers):
#        Encoded_Table.append(Numbers[new_index])
    


#def RemoveNumbersFromString(number, shift):
#    new_index = Numbers.index(number) - shift
#    
#    if new_index < 0:
#        new_index = (new_index * -1)
#
#        if new_index > len(Numbers):
#            new_index = (new_index % 10)
#
#        Decoded_Table.append(Numbers[new_index])
#    else:
#        Decoded_Table.append(Numbers[new_index])





def EncryptCeaserCypher(String):
    Encoded_String = ""
    Shift_Amount = random.randint(1, len(Characters))


    for letter in String:
        if letter == " ":
            Encoded_Table.append(letter)

        elif letter in Characters:
            AddToString(letter, True, Shift_Amount)
        elif letter.isupper():
            AddToString(letter, False, Shift_Amount)
        elif letter in Numbers:
            AddToStringNumbers(letter, Shift_Amount)
        elif letter in Special_Characters:
            pass

    for character in Encoded_Table:
        Encoded_String += character

    if len(Encoded_String) > 0:
        print(f"\nHere's your encoded result: {Encoded_String}, your shift is {Shift_Amount}")



def DecryptCeaserCypher(String):
    Shift = int(input("\nPlease enter the shift number given to you: "))
    Decoded_String = ""

    for letter in String:
        if letter == " ":
            Decoded_Table.append(letter)

        elif letter in Characters:
            ReverseLetters(letter, Shift, True)
        elif letter.isupper():
            ReverseLetters(letter, Shift, False)

    for data in Decoded_Table:
        Decoded_String += data

    if len(Decoded_String) > 0:
        print(f"\nHere's your decoded result: {Decoded_String}")





while Continue_Running:
    index = 0

    print(title)
    print("Choose Your Encryption Method.")

    def DecideEncryption(Method, Choice, String):
        Method = Methods[Method]
        Choice = Choices[Choice]

        Encode_Step_One = String.encode('utf-8')

        if Choice == "Encryption":
            if Method[0] == "C":
                EncryptCeaserCypher(String)      


            if Method[0] == "B":
                encoded_byte = Encode_Step_One
                encoded_bytes = base64.b64encode(encoded_byte)
                encoded_string = encoded_bytes.decode('utf-8')

                print(f"\nHere's your encoded result: {encoded_string}")
        else:
            if Method[0] == "C":
                DecryptCeaserCypher(String)

            if Method[0] == "B":
                encoded_byte = Encode_Step_One
                encoded_bytes = base64.b64decode(encoded_byte)
                encoded_string = encoded_bytes.decode('utf-8')

                print(f"\nHere's your decoded result: {encoded_string}")



    def ChooseMethod():
        global My_Method
        global index

        Colors = ["\x1b[34m", "\x1b[32m"]

        for Method in Methods:
            index += 1
            new_index = str(index) + ". "
            color = Colors[index - 1]

            print(f"{color}{new_index}{Method}")

        index = 0
        My_Method = int(input("\x1b[31m\n")) - 1


    def ChooseType():
        global My_Choice
        global index

        print("\nChoose your cryption type!")

        for Choice in Choices:
            index += 1
            new_index = str(index) + ". "

            print(new_index, Choice)

        My_Choice = int(input("\n")) - 1

    ChooseMethod()
    ChooseType()

    User_String = str(input("\nInput ur text here:\n"))

    DecideEncryption(My_Method, My_Choice, User_String)

    Continue = str(input("Would you like to continue? Type 'Y' or 'N'. ")).lower()

    if Continue[0] == "y":
        for a in range(1, 100):
            print("\n")
            Encoded_Table.clear()
            Decoded_Table.clear()

            My_Method = None
            My_Choice = None
            User_String = None
    else:
        Continue_Running = False
        break

