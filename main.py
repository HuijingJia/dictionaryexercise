from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo) # print logo for the bidding

def find_the_highest_bidding():
    winner = ""
    amount = 0
    for bidder in bidder_Dict:
        price = bidder_Dict[bidder]
        if price > amount:
          amount = price
          winner = bidder
    print(f"The winner is {winner}, and the bidding amount is {amount}.")
bidder_Dict = {} # create a dictionary to store key and value
bidding = True # create a boolean
while bidding:
  name = input("What is your name?: ")
  price = int(input("How much you want to bid?: $"))
   # create a dictionary
  bidder_Dict[name] = price #name will be the key and price will be the value of the key; this is something I think about for a long time how to assign.
  inquiry = input("Are there others? Type Yes or No: ").lower()
  
  if inquiry == "yes":
      clear()
      
  else:
      bidding = False
      find_the_highest_bidding()
      shouldcontinue = input("Do you want once again?: YES or NO?: ").lower()
      if shouldcontinue == "yes":
          bidding = True
      else:
          print("Thank you! You will succeed!")
        
      
      
  
  




