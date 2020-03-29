#napisz program obliczający średnią wartość temperatury w danym tygodniu
# na podstawie temperatur wprowadzonych przez użytkownika

x = 7
temperatura = 0 # wartość startowa temperatury

while x > 0:
    t = int(input("Podaj temperaurę: "))
    x -= 1
    temperatura += t  # suma wprowadzonych

print(f"Średnia temperatur to: {temperatura / 7:.2f} ")