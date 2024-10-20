import random
## A
droga = random.randint(1, 1000)
spalanie = float(input("Średnie spalanie [l/100km]:"))
cena_paliwa = float(input("Cena paliwa [zł/l]:"))
zuzycie = droga * spalanie * 0.01
koszty = zuzycie * cena_paliwa

print(f"Droga [km]: {droga}\nZużycie paliwa [l]: {zuzycie}\nKoszty [zł]: {koszty}")