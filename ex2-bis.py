def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

numbers = []
n = int(input("Combien de nombres voulez-vous entrer? "))
for i in range(n):
    number = int(input(f"Entrez le nombre {i + 1}: "))
    numbers.append(number)

median_value = calculate_median(numbers)

print("La médiane des nombres entrés est :", median_value)
