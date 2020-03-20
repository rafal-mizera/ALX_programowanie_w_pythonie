

#Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI, oraz
#podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
# BMI = masa(kg) / wzrost(m)**

masa = input("Podaj swoją mase w kg: ")
wzrost = input("Podaj swój wzrost w cm: ")

BMI = float(masa) / (float(wzrost) / 100) **2


print(f"Twoje BMI wynosi: {BMI:.2f}")

if BMI < 16:
    warunek = ("Masz niedowagę. Powinieneś przytyć")
if BMI >= 16 and BMI < 17:
    warunek = "Masz nadwagę. Powinieneś schudnąć"
if BMI >= 17 and BMI < 18.49:
    warunek = "Masz niedowagę. Powinieneś przytyć"
if BMI >= 18.5 and BMI < 24.99:
    warunek = "Twoja waga jest odpowiednia"
if BMI >= 25 and BMI < 29.99:
    warunek = "Masz nadwagę. Powinieneś schudnąć"
if BMI >= 30 and BMI < 34.99:
    warunek = "Masz nadwagę. Powinieneś schudnąć"
if BMI >= 35 and BMI < 35:
    warunek = "Masz nadwagę. Powinieneś schudnąć"
if BMI >= 35:
    warunek = "Masz nadwagę. Powinieneś schudnąć"

print(warunek)

