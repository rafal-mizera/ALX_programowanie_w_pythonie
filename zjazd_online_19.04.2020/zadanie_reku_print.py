# def print_stars(n):
#     """Rekurencyjne wypisywanie n linii z gwiazdką."""
#     if n > 0:
#         print ( "*" )
#         print_stars(n-1)
#
# print_stars(4)

def reku_print(napis):
     if napis:
        x = 0
        print(napis[x])
        reku_print(napis.replace(napis[x],""))
     else:
        return













reku_print("agnieszka")




