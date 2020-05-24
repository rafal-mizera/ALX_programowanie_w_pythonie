import time


def mierz_czas(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(time.time() - start)
        return result
    return wrapper()


@mierz_czas
def milion_kwadratow():
    return len([x**2 for x in range(1000000)])


# @mierz_czas
# def kwadraty(n):
#     return len([x**2 for x in range(n)])


print(milion_kwadratow())



