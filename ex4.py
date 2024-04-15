def count_letters_and_digits(s):
    letter_count = 0
    digit_count = 0

    for char in s:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1

    return letter_count, digit_count


input_string = input("Saisissez une chaîne: ")
letters, digits = count_letters_and_digits(input_string)

print("Lettres", letters)
print("Chiffres", digits)
