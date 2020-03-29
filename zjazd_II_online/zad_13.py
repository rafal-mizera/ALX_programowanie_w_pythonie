#napisz program obliczający średnią wartość temperatury w danym tygodniu
# na podstawie temperatur wprowadzonych przez użytkownika

x = 7
temperatura = 0

while x > 0:
    t = int(input("Podaj temperaurę: "))
    x -= 1
    temperatura += t  # suma wprowadzonych

print(f"Średnia temperatur to: {temperatura / 7} ")