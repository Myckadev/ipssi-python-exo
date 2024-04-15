def length_of_last_word(s):
    # Éliminer les espaces en début et fin de chaîne
    s = s.strip()

    # Séparer la chaîne en une liste de mots
    words = s.split()

    # Si la liste des mots n'est pas vide, retourner la longueur du dernier mot
    if words:
        return len(words[-1])

    # Si la liste est vide (cas d'une chaîne ne contenant que des espaces), retourner 0
    return 0


# Exemple 1
print(length_of_last_word("Hello World"))  # Output: 5

# Exemple 2
print(length_of_last_word(" Envole-moi vers la lune "))  # Output: 4

# Exemple 3
print(length_of_last_word("Luffy est toujours Joyboy"))  # Output: 6

# autre exemple complètement nawal c:
print(length_of_last_word("Oui oui la france c'est les          baguettes"))
