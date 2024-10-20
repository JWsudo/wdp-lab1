import math

print("Rozwiązywanie równiania ax2 + bx + c = 0")
a = float(input("Podaj współczynnik a:"))
b = float(input("Podaj współczynnik b:"))
c = float(input("Podaj współczynnik c:"))

if (a == 0):
    if (b == 0):
        if (c == 0):
            print("Równanie tożsamościowe")
            exit(0)
        else:
            print("Równanie nie ma rozwiązania")
            exit(0)
    else:
        x = -c/b
        print(f"Rozwiązanie x={x}")
        exit(0)

delta = b ** 2 - (4 * a * c)

if delta > 0:
    x1 = ((-b + math.sqrt(delta)) / (2 * a))
    x2 = ((-b - math.sqrt(delta)) / (2 *a))
    print(f"Rozwiązania: x1={x1}, x2={x2}")
    exit(0)
elif delta == 0:
    x = -b / (2 * a)
    print(f"Rozwiązanie: x={x}")
    exit(0)
else:
    print("Delta ujemna, brak rozwiązań!")