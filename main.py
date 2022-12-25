import clear

auction_start = True
auction = {}

def bidder_win(highest_bid):
    amount = 0
    winner = ""

    for bidder in highest_bid:
        bidder_bid = highest_bid[bidder]
        if bidder_bid > amount:
            amount = bidder_bid
            winner = bidder
    print(f"The winner is: {winner} with the highest bid {amount} $")


while auction_start:

    name = input("What is your name?: ").capitalize()
    bid = int(input("What is your bid amount?: "))

    auction[name] = bid
    print(auction)
    end_auction = input("Are there another bidder? 'y' or 'n': ")
    if end_auction == "y":
        auction_start = True
    else:
        bidder_win(highest_bid=auction)
        auction_start = False
