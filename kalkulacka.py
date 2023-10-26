x = input("zadaj cislo x: ")
operacia = input('zadaj operaciu: ')
y = input('zadaj cislo y: ')

# Skontroluj, či sú zadané hodnoty čísla.
if x.isnumeric() and y.isnumeric():
    x = float(x)
    y = float(y)

    if operacia == '+':
        vysledok = x + y
    elif operacia == '-':
        vysledok = x - y
    elif operacia == '*':
        vysledok = x * y
    elif operacia == '/':
        if y == 0:
            vysledok = "Si si myslel co."
        else:
            vysledok = x / y
    else:
        vysledok = "Neznama operacia"
    
    print("Vysledok:", vysledok)
else:
    print("bruh toto je kalkulacka.")
