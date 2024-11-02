from urllib.response import addbase

print(" how many numbers you want to addb")
number =int(input())
sum_of_numbers = 0
total=0
while sum_of_numbers < number:
    print(f"please enter number{sum_of_numbers + 1} of {number}:")
    sum_number = int(input())
    total = total + sum_number
    sum_of_numbers = sum_of_numbers + 1

print(f"... Done! Total of all numbers is {total}.")


