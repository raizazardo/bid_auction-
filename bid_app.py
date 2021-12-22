from replit import clear
from art import logo

print (logo)
bids = {}
def find_highest_bideer (biddind_record):
	highest_bid = 0 
	winner = ""
	for bidder in biddind_record: 
		bid_amount = biddind_record[bidder] 
		if bid_amount > highest_bid: 
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of $ {highest_bid}")

bidding_finished = False
while not bidding_finished:
	name = input("What is your name?: ")
	price = input(int("what is your bid?: $"))
	bids[name] = price
	should_continue = input("There are more people participating? type 'y' or 'n'\n")
	if should_continue == "n":
		bidding_finished = True
		find_highest_bideer(bids)
	elif should_continue == "y":
		clear()
	

