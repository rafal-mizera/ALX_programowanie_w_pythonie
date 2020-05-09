# def decrement(n):
#     if n == 0:
#         print(0)
#         return
#     print(n)
#     decrement(n-1)
#
# decrement(10)

def silnia(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Nie można wyświetlić silni"
    else:
        return n * silnia(n - 1)


print(silnia(3))

def silnia_test():
    assert silnia(5) == 120
    assert silnia (3) == 6
    assert silnia (0) == 1


