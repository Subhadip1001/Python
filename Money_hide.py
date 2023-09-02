print("\n")
row1 = ['🤔','🤔','🤔']
row2 = ['🤔','🤔','🤔']
row3 = ['🤔','🤔','🤔']

matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print("\n")

positon = input("Enter number where you hide money : ")
row_number = int(positon[0])
colum_number = int(positon[1])
row_selected = matrix[row_number-1]
row_selected [colum_number-1] = '🤑'
print("\n")

print(f"{row1}\n{row2}\n{row3}")
print("\n")