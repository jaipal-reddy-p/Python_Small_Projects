print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Small, Mediam, or Large \n")
add_pepperoni = input("Do you want pepperoni? Yes or No \n")
extra_cheese = input("Do you want extra cheese? Yes or No \n")
bill = 0

if size == "Small":
  bill += 15
elif size == "Mediam":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Yes":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Yes":
  bill += 1
  
print(f"Your final bill is: ${bill}.")




