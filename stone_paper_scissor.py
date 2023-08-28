import random
print("\n")
print("For 'Stone' enter 0 ")
print("For 'Paper' enter 1 ")
print("For 'Scissor' enter 2 ")
print("\n")

computer_choice = random.randint(0,2)
# print(computer_choice)
manual_choice = int(input("Enter your choice : "))

if(computer_choice == 0 and manual_choice == 0):
    print("DRAW")
elif(computer_choice == 0 and manual_choice == 1):
    print("YOU WIN")
elif(computer_choice == 0 and manual_choice == 2):
    print("COMPUER WIN")
elif(computer_choice == 1 and manual_choice == 0):
    print("COMPUTER WIN")
elif(computer_choice == 1 and manual_choice == 1):
    print("DRAW")
elif(computer_choice == 1 and manual_choice == 2):
    print("YOU WIN")
elif(computer_choice == 2 and manual_choice == 0):
    print("YOU WIN")
elif(computer_choice == 2 and manual_choice == 1):
    print("COMPUTER WIN")
elif(computer_choice == 2 and manual_choice == 2):
    print("DRAW")
else:
    print("You enter a wrong input !")


print("\n")