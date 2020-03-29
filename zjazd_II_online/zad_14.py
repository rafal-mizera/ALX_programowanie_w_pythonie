min_x = None
max_x = None

while True:
    number = input("wprowadź liczbę lub x by zakonczyc: ")
    if number == "x":
        break
    number = int(number)
    if min_x is None or number < min_x:
        min_x = number
    if max_x is None or number > max_x:
        max_x = number

print(f"Wartość maksymalna: {max_x}")
print(f"Wartość minimalna: {min_x}")
