def exchange(amount):
    coin500 = amount // 500
    A = amount % 500

    coin100 = A // 100
    A = A % 100

    coin50 = A // 50
    A = A % 50

    coin10 = A // 10

    print("500원 동전의 개수:", coin500)
    print("100원 동전의 개수:", coin100)
    print("50원 동전의 개수:", coin50)
    print("10원 동전의 개수:", coin10)




def get_integer(prompt):
    res=int(input(prompt))
    return res

amount = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(amount)
    