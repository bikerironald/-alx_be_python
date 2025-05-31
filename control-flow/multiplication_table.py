# Use a for loop to generate and print the multiplication table for a given number.

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 10):
    print(f"{number} x {i} = {number * i}")
