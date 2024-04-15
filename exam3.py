def roman_to_int(s):
    # Créer un dictionnaire pour les valeurs des chiffres romains
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    length = len(s)

    for i in range(length):
        value = roman_values[s[i]]

        # Vérifier si le caractère actuel doit être soustrait
        if i + 1 < length and roman_values[s[i + 1]] > value:
            total -= value
        else:
            total += value

    return total


# Exemple 1
print(roman_to_int("III"))  # Output: 3

# Exemple 2
print(roman_to_int("LVIII"))  # Output: 58

# Exemple 3
print(roman_to_int("MCMXCIV"))  # Output: 1994

# Autre exemple aléatoire
print(roman_to_int("MMMMCXIV"))