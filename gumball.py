def collect_coins_from_user():
   total = 0
   acceptable_coin = [0.05, 0.1, 0.25]
   cont = "yes"
   while True:
       coin = float(input("Please insert ur coin Nickel(.05) / Dime(.1) / Quarter(.25) : "))
       if coin in acceptable_coin:
           total = coin + total
           if total > 100:
                 print("Inserted coins exceeds the limit")
                 return(total)
           print("Total value of coins inserted is :${}".format(total))
           cont = input("Do you want to insert More Coins [yes/no]:")
       else:
           print("!!!!You can only insert Nickel / Dime / Quarter!!!!")
       if cont == "no":
           return(total)
           break

def dispense_dict(total_paid,gumball_dict):
   gum_ball_colors = gumball_dict.keys()
   cont = "yes"
   rem_balance = total_paid
   while True:
       lever_choice = input("Press the lever to Dispense the Gumball of your choice {}:".format(gumball_dict))
       #check if the user selected the right lever for dispencing the gumballs
       if lever_choice in gum_ball_colors:
           for i in gum_ball_colors:
               if lever_choice == i and rem_balance >= gumball_dict[i]:
                   print("Dispencing {} GumBall".format(i))
                   rem_balance = total_paid - gumball_dict[i]
               elif lever_choice == i:
                   print("Insufficient Funds to dispense {} GumBall".format(i))               
       else:
           print("invalid selection, please try again")
           continue
       cont = input("Do you want to press the Dispenser lever again [yes/no]:")
       if cont == "no":
           return (rem_balance)
           break

if __name__ == "__main__":
   # we have red gumball each worth nickel and yellow gumball each worth dime,
   #Just keep adding to the list,there is no need to modify the code.
   gumball_dict = {'red': 0.05, 'yellow': 0.1}
   #Function to collect coins from the user
   total_paid = collect_coins_from_user()
   print(total_paid)
   #Function to Dispense the gumballs to the end users and return the balance amount
   bal = dispense_dict(total_paid,gumball_dict)
   print("Thank you for visiting us Please Collect the change:${}".format(bal))
