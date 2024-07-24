import random

repeat = True

art = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


while repeat:
    YesOrNo = input("\nDo you want to play a game of Blackjack? Type 'Y' or 'N' ").lower()

    if YesOrNo == "y":
        for i in range(1,100):
            print("\n")
            
        repeat = True
        MyList = []
        TheirCards = []
    elif YesOrNo != "y":
        repeat = False

    def GeneratePlayerCards(wantedCards):
        for i in range(0,wantedCards):
            cardGenerated = random.randint(1,10)
            MyList.append(cardGenerated)

    def GenerateComputerCards():
        cardGenerated = random.randint(1,10)
        TheirCards.append(cardGenerated)
            
    def ReturnPlrScore(chosenList):
        return sum(chosenList)

    def CheckSum(theList):
        summedList = sum(theList)
        
        if summedList > 21:
            return True

    def FindLoser(l1, l2):
        l1sum = sum(l1)
        l2sum = sum(l2)
        
        if l1sum > l2sum and l1sum < 21:
            print("\nYou Win!")
        elif l2sum > l1sum and l2sum < 21:
            print("\nComputer wins!")

    print(art)
    GeneratePlayerCards(2)
    GenerateComputerCards()
    
    FirstComputerCard = TheirCards[0]
    
    print(f"\nYour cards: {MyList}, current score: {ReturnPlrScore(MyList)}")
    print(f"Computer's first card: {FirstComputerCard}")
    GameInProgress = True
    
    while GameInProgress:
        greed = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
        if greed == "y":
            GeneratePlayerCards(1)
            print(f"\nYour current hand: {MyList}, current score: {ReturnPlrScore(MyList)}")
        
            GenerateComputerCards()
            print(f"Computer's current hand: {TheirCards}, current score: {ReturnPlrScore(TheirCards)}")
        

        elif greed == "n":
            GameInProgress = False
            GenerateComputerCards()
            
            print(f"\nYour current hand: {MyList}, current score: {ReturnPlrScore(MyList)}")
        
            print(f"Computer's current hand: {TheirCards}, current score: {ReturnPlrScore(TheirCards)}")
            
            FindLoser(MyList, TheirCards)
            break
            

            
        if CheckSum(MyList) == True:
            print("Computer Wins!")
            GameInProgress = False
            
        elif CheckSum(TheirCards) == True:
            print("You win!")
            GameInProgress = False
