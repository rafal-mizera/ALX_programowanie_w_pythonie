elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]
elementy = set(elementy)
print(f"Unikalne elementy zbioru 1: {len(elementy)}")

elementy2 = {"aaa", "aba", "ccc"}
elementy2 = set(elementy2)
print(f"Unikalne elementy zbioru 2: {len(elementy2)}")

print(f"Wspólnych elementów było: {len(elementy & elementy2)}")
print(f"Elementy wspólne tych zbiorów to : {elementy & elementy2}")


