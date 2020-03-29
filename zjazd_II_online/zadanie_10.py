first_num = int(input("Podaj pierwszą liczbę: "))
second_num = int(input("Podaj drugą liczbę: "))
operation = input("Podaj rodzaj operacji: ")

if operation == "+":
    print(f"Wynik: {first_num + second_num}")
elif operation == "-":
    print(f"Wynik: {first_num - second_num}")
elif operation == "*":
    print(f"Wynik: {first_num * second_num}")
elif operation == "/" and second_num > 0:
    print(f"Wynik: {first_num / second_num}")
elif operation == "/" and second_num == 0:
    print(f"Nie można dzielić przez 0")
else:
    print("Podałeś błedny znak operacji")