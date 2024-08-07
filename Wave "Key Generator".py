import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "7", "8", "9"]
Exit = False

print("hello this is best wave key gen 100%\n")
decChoice = input("Do you wish to run key generator?? ")


while Exit != True:
    GeneratedKey = []
    PrintableKey = ""

    def CreateKi():
        print("Key is being generated...")
        keylength = 0
        while keylength != 20:
                
            if keylength == 5 or keylength == 10 or keylength == 15 or keylength == 20:
                GeneratedKey.append("-")
            
            randomizer = random.randint(0, 1)
            randomizer2 = random.randint(0, 1)
            LetterOrNumber = 0
        
            if randomizer == 0:
                LetterOrNumber = "Letter"
                RandomizedLetter = letters[random.randint(0,25)]
                if randomizer2 == 0:
                    CapitalizedLetter = RandomizedLetter.upper()
                    GeneratedKey.append(CapitalizedLetter)
                    
                elif randomizer2 == 1:
                    GeneratedKey.append(RandomizedLetter)
                    
                keylength += 1 
            
            elif randomizer == 1:
                LetterOrNumber = "Number"
                RandomizedNumber = numbers[random.randint(0,8)]
                GeneratedKey.append(RandomizedNumber)
                
                keylength += 1
        
        

    if decChoice.lower() == "yes":
        CreateKi()
        for i in GeneratedKey:
            PrintableKey = PrintableKey + "".join(i)
        print(f"Your final key is: {PrintableKey}")
        RepeatChoice = input("\nWould you like to generate another key? ")
        
        if RepeatChoice.lower() == "yes":
            Exit = False
        else:
            Exit = True
            
        
