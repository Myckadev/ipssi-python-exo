def convert_temperature(temp):
    degree = int(temp[:-1])
    unit = temp[-1].upper()

    if unit == 'F':
        converted = (degree - 32) * 5 / 9
        return f"La température en Celsius est de {int(converted)} degrés."

    elif unit == 'C':
        converted = (degree * 9 / 5) + 32
        return f"La température en Fahrenheit est de {int(converted)} degrés."

    else:
        return "Input incorrect. Utilisez 'C' pour Celsius ou 'F' pour Fahrenheit à la fin du nombre."

temp_input = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
print(convert_temperature(temp_input))
