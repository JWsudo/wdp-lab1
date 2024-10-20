print("Kalkulator\n")
wybor = int(input("Wybierz operację:"
                  "\n1. Dodawanie"
                  "\n2. Odejmowanie"
                  "\n3. Mnożenie"
                  "\n4. Dzielenie"
                  "\n5. Potęgowanie\n..."))
a = float(input("Podaj pierwszą liczbę"))
b = float(input("Podaj drugą liczbę"))
match wybor:
    case 1:
        wynik = a + b
        print(f"Dodawanie, wynik={wynik}")
    case 2:
        wynik = a - b
        print(f"Odejmowanie, wynik={wynik}")
    case 3:
        wynik = a * b
        print(f"Mnożenie, wynik={wynik}")
    case 4:
        if (b != 0):
            wynik = a / b
            print(f"Dzielenie, wynik={wynik}")
        else:
            print("Nie można dzielić przez zero!")
    case 5:
        wynik = a ** b
        print(f"Potęgowanie, wynik={wynik}")
    case _:
        print("Wybrano nieistniejącą opcję!")
