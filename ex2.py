def find_median(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]

# Inputs
first_number = int(input("Input the first number: "))
second_number = int(input("Input the second number: "))
third_number = int(input("Input the third number: "))

median = find_median(first_number, second_number, third_number)

print("La mediane est :", median)
