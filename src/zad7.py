print("Rozwiązywanie równiania ax + b = 0")
a = float(input("Podaj współczynnik a:"))
b = float(input("Podaj współczynnik b:"))

if(a == 0):
    if(b == 0):
        print("Równanie tożsamościowe, każda liczba jest rozwiązaniem")
        exit(0)
    else:
        print("Równianie nie ma rozwiązania!")
        exit(0)
else:
    x = -b/a
    print(f"rozwiązanie to liczba: {x}")
