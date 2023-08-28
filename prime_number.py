def prime_number(number):
    count = 0
    for i in range(2,number):
        if(number % i == 0):
            count+=1
    if(count == 0):
        print("%d is not a prime number"%number)
    else:
        print("%d is a prime number"%number)

number = int(input("Enter number which you check its prime or not : "))
prime_number(number)
