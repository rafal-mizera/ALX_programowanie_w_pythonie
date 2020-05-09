#Zaimplementuj funkcję formatującą podane napisy.
#>>> formatuj('koszt $cena PLN','kwota $cena brutto',cena=10 )
#'koszt 10 PLN\nkwota 10 brutto'



def formatuj(*args, **kwargs):
    text = "\n".join(args)
    for kwarg, arg in kwargs.items():
        text = text.replace("$" + kwarg, str(kwarg))

    return text


formatuj("koszt $cena PLN','kwota $cena brutto',cena=10")







def test_formatowania():
    formatuj("koszt $cena PLN','kwota $cena brutto',cena=10" ) == 'koszt 10 PLN\nkwota 10 brutto'
    formatuj("koszt $cena PLN','kwota $cena brutto',cena=15" ) == 'koszt 15 PLN\nkwota 15 brutto'



