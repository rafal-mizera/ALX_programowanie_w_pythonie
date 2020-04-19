#napisz program obliczający średnią wartość temperatury w danym tygodniu
# na podstawie temperatur wprowadzonych przez użytkownika

x = 7           # ilość dni "obroty pętli" ###W TYM WYPADKU 7 JEST WARTOŚCIĄ STARTOWĄ GDYŻ x -=1
temperatura = 0 # wartość startowa temperatury

while x > 0:   # wykonuj dla x większego od 0
    t = int(input("Podaj temperaurę: ")) # użytkownik podaje t, czyli temperaturę z konkretnego dnia
    x -= 1 # o jaką wartość przeskakuje pętla
    temperatura += t  # suma wprowadzonych temperatur rośnie o pojedynczo wprowadzone t

print(f"Średnia temperatur to: {temperatura / 7:.2f} ")

# Napisz program obliczający średnią ocen na podstawie ocen wprowadzonych przez ucznia. Maksymalną liczbą wprowadzonych
# ocen niech będzię 10, jeżeli ocen było mniej niech "koniec" zatrzyma wpisywanie

grades_counter = 0
grades_sum = 0

while grades_counter < 10:
    grade = input("Podaj ocenę: ")
    if grade == "koniec":
        break
    else:
        grade = int(grade)
        grades_counter += 1
        grades_sum += grade

print(f"Twoja średnia ocen to: {grades_sum / grades_counter}")


