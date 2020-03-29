#for y in "123":
#    for x in "abc":
#           break
#      print(x + y)

dane = [-1, 21, -15, 22, -4, -5, 6, 19, 28]
dodatnie = 0
ujemne = 0

for x in dane:
    if x < 0:
        ujemne += 1
    if x > 0:
        dodatnie += 1

print("Dodatnie:", dodatnie , "ujemne:", ujemne)







