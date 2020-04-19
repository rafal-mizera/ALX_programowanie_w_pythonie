#Napisz program sprawdzający czy podana przez użytkownika liczba jest podzielna przez 2, podzielna przez 3 i większa od 10
# lub jest to liczba 7

liczba = int(input("Podaj dowolną liczbę całkowitą: "))

print(f"""
Liczba jest podzielna przez 2, 
podzielna przez 3
i większa od 10
lub jest to liczba 7:
{liczba / 2 == 0 and liczba / 3 == 0 and liczba > 10 or liczba == 7} """)

#Napisz program sprawdzający czy podana przez użytkownika liczba jest podzielna przez 6, jest większa od 30 i mniejsza od 60 lub
#jest to liczba 15

num = int(input("Podaj liczbę całkowitą: "))

print(f"""
Podana liczba jest podzielna przez 6,
jest większa od 30 
i mniejsza od 60
lub jest to
liczba 15:
{'x' * 50}
{num % 6 == 0 and num > 30 and num < 60 or num == 15}""")