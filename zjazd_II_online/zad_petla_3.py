#for y in "123":
#    for x in "abc":
#           break
#      print(x + y)
# Niech program policzy ile w podanej liście jest liczb dodatnich a ile ujemnych

dane = [-1, 21, -15, 22, -4, -5, 6, 19, 28]
dodatnie = 0                                    # tworzymy dwie listy do których będą dodawane liczby dodatnie lub ujemne
ujemne = 0

for x in dane:                                  # dla elementu x będącego częścią listy dane:
    if x < 0:                                     # jeśli x jest mniejszy od zera to
        ujemne += 1                             # do zbioru ujemnych dodajemy 1
    if x > 0:                                     # jeśli większy
        dodatnie += 1                             # to do dodatnich

print("Dodatnie:", dodatnie , "ujemne:", ujemne)

collection = ["aaa", "traktor", "niebieski", 1, 2, 4]
strings = []
numbers = []

for x in collection:
    if x == str(x):
        strings.append(x)
    else:
        numbers.append(x)
print(f"Napisy to: {strings} a liczby: {numbers}")











