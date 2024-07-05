logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
EndBid = False


BidInfo = {
     "Names": [],
     "Bids": [],
}


while EndBid != True: 
    print(f"{logo} \nWelcome to the secret auction!")

    name = str(input("What is your name?: "))
    bid = int(input("What is your bid amount?: $"))
    OtherBidders = str(input("Are there any other bidders? Yes or No. ")).lower()



    BidInfo["Names"].append(name)
    BidInfo["Bids"].append(bid)
    

    def FindHighestBid(list):
        PreviousBid = 0
        for bid in list:
            if bid > PreviousBid:
                PreviousBid = bid
                
        return PreviousBid


    if OtherBidders == "no" or OtherBidders != "yes":
            
        HighestBid = FindHighestBid(BidInfo["Bids"])
        HighestBidIndex = BidInfo["Bids"].index(HighestBid)
        CorrespondingName = BidInfo["Names"][HighestBidIndex]
        
        print(f"{CorrespondingName} is the highest bidder with ${HighestBid}!")
        EndBid = True    
    else:
        for i in range(1,25):
            print("\n")
        continue
