bisiesto = lambda year: True if year % 4 == 0 else False
year = int(input('Digite año: '))
print(year,'es bisiesto') if bisiesto(year) else print(year,'no es bisiesto')