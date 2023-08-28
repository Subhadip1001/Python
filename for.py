number = int(input("Enter number : "))
for number in range(1,number-1):
                 # (1,number) print = 1,2,...,n-1
                 # (0,number) print = 0,1,2,....,n-1
                 # (0,number+1) print = 0,1,2,....,n
                 # (0,number-1) print = 0,1,2,...,n-2

    print(number)