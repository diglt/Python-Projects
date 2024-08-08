import random
import DataStorage

AccountTable = DataStorage.data
Score = 0
IsRunning = True


def FindRandomAccount(RandomIndex):
    for Index, Value in enumerate(AccountTable):
        if Index == RandomIndex:
            RandomAccount = Value
            return RandomAccount


def FindFactFromAccount(passed, WantedFact):
    for Info, Value in passed.items():
        if Info == WantedFact:
            return Value


def ReturnRandomCelebrity():
    RandomIndex = random.randint(1, len(AccountTable))
    RandomAccount = FindRandomAccount(RandomIndex)
    RandomAccountTable = DataStorage.data[RandomAccount]
    KnownFor = FindFactFromAccount(RandomAccountTable, "known_for")
    LocationFrom = FindFactFromAccount(RandomAccountTable, "birth_country")
    FollowerCount = FindFactFromAccount(RandomAccountTable, "followers")
    return RandomAccount, KnownFor, LocationFrom, FollowerCount


while IsRunning:
    RandomAccount1, KnownFor1, LocationFrom1, FollowerCount1 = ReturnRandomCelebrity()

    print(DataStorage.logo)

    if Score >= 1:
        print(f"Current score is: {Score}")

    CompareA = f"Compare A: {RandomAccount1}, who is known for {KnownFor1}, from {LocationFrom1}\n"
    print(CompareA)

    print(DataStorage.VS)

    SecondAccount, KnownFor2, LocationFrom2, FollowerCount2 = ReturnRandomCelebrity()

    CompareB = f"Against B: {SecondAccount}, who is known for {KnownFor2}, from {LocationFrom2}\n"
    print(CompareB)

    HighestFollowers = None

    if FollowerCount1 > FollowerCount2:
        HighestFollowers = FollowerCount1
    else:
        HighestFollowers = FollowerCount2

    Choice = str(input("Who has more followers? Type 'A' or 'B' ")).lower()

    if Choice == "a" and HighestFollowers == FollowerCount1 or Choice == "b" and HighestFollowers == FollowerCount2:
        Score += 1

    else:
        print("You loose.")
        PlayAgain = str(input("Would you like to play again? 'Y' or 'N' ")).lower()

        if PlayAgain == "y":
            continue
        else:
            IsRunning = False

