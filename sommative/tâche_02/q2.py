# Nom: Ton Nom
# Description: Convertit une température Celsius en Fahrenheit et en Kelvin

celsius = float(input("Entrez une température en Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(celsius, "°C =", fahrenheit, "°F")
print(celsius, "°C =", kelvin, "K")
