import random

options = ["snake", "water", "gun"]
compter_choice = random.choice(options)
your_choice = input("Enter your choice: ")

print(f"Computer chose {compter_choice}")

if(your_choice == "snake" and compter_choice == "water"):
    print("You win")
elif(your_choice == "snake" and compter_choice == "gun"):
    print("You lose")
elif(your_choice == "snake" and compter_choice == "snake"):
    print("Uh oh! its a tie.")

if(your_choice == "gun" and compter_choice == "water"):
    print("You Lose")
elif(your_choice == "gun" and compter_choice == "gun"):
    print("Uh oh! its a tie.")   
elif(your_choice == "gun" and compter_choice == "snake"):
    print("You lose")

if(your_choice == "water" and compter_choice == "water"):
    print("Uh oh! it's a tie.")
elif(your_choice == "water" and compter_choice == "gun"):
    print("You win")   
elif(your_choice == "water" and compter_choice == "snake"):
    print("You lose")






