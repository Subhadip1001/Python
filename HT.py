import random
your = input("Enter your choice (Head / Tails) :")

l= ['Head', 'tails']

if(your== random.choice(l)):
    print("You Win")
else:
    print(random.choice(l))
    print("You loss")


