
# a
print([(x / 10) for x in range(0,11)])

# b
print([[x, x ** 2, x ** 3] for x in range(-10,10)])

# c
napisy = ["xxxx", "yyyy", "yy"]

print({napis: len(napis) for napis in napisy})


# d

print([x * 10 for x in range(0,10,2)])

# e

print([[x/2, x/5] for x in range(4,100,5)])

# f
slowka = ["mama", "tata", "dom"]

print({napis: napis[0] for napis in slowka})
