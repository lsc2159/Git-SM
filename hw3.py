def get_fixed_pirce(rate, price):
    return int(price/(1-rate/100))

def main():
    rate=int(input('할인율은?'))
    price_A=int(input('A 상품의 할인된 가격은?'))
    price_B=int(input('B 상품의 할인된 가격은?'))

    S_price_A=get_fixed_pirce(rate,price_A)
    S_price_B=get_fixed_pirce(rate,price_B)

    print('A 상품의 정가는', S_price_A, '원')
    print('B 상품의 정가는', S_price_B, '원')

if __name__=='__main__':
    main()

