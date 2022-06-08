from click import clear
from art import logo

print(logo)


all_bids = {
    
}
max_bid = 0

end_of_bid = False

while not end_of_bid:
    user_name = input("What is your name? : ")
    user_bid = int(input("Please enter your bid amount: $"))
    
    if user_bid > max_bid:
        max_bid = user_bid
        max_user = user_name

    all_bids[user_name] = user_bid
    
    status = input("Is there another bider? Type yes or no: ").lower()

    if status == "no":
        end_of_bid = True
    elif status =="yes":
        clear()

print(f"End  of the bid.\nThe winner is {max_user} with a bid of ${all_bids[max_user]}")