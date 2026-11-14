import random

'''
1 = water
0 = gun
-1 = snake'''

compter_choice = random.choice([0, 1, -1]) #random module selects a random value from the given list.

your_string = input("Enter your choice ") #enter "g", "w", "s".

options_dictionary ={"w" : -1 , "g" : 0, "s" : 1 } #1. so user wont have to write the whole word, just one letter like "s"
your_choice = options_dictionary[your_string] #2. users key like "s" is converted to its value  i.e 1 and then stored in your_choice
reverse_options_dict = {-1 : "water", 0 : "gun", 1 : "snake"} #3. users converted value i.e 1 then gets the whole word i.e "snake" from reverse_options_dict


print(f"Your choice is {reverse_options_dict[your_choice]}\nComputer's choice is {reverse_options_dict[compter_choice]}") #4. users word is printed through reverse_options_dict[your_choice]

if(your_choice == compter_choice):
    print("Its a tie")
else:
    if(your_choice == 1 and compter_choice == -1): # your_choice - computer choice ie 1 - (-1) = 2
        print("You win")

    elif(your_choice == 1 and compter_choice == 0): # 1 - 0 = 1
        print("You lose")

    elif(your_choice == 0 and compter_choice == -1): # 0 -(-1) = 1
        print("You Lose")

    elif(your_choice == 0 and compter_choice == 1): #0 - 1 = -1
        print("You Win")

    elif(your_choice == -1 and compter_choice == 0): #-1 - 0 = -1
        print("You win") 

    elif(your_choice == -1 and compter_choice == 1): #-1 - 1 = -2
        print("You lose")

    else: 
        print("Invalid choice, Please enter snake, water, or gun")
