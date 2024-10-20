# zad 6
droga = float(input("Przebyta droga [km]:"))
spalanie = float(input("Średnie spalanie [l]:"))
cena_paliwa = 6.5

zuzycie = droga * spalanie * 0.01
koszty = zuzycie * cena_paliwa

print(f"Zużycie paliwa [l]: zużycie\nKoszty [zł]: {koszty}")
