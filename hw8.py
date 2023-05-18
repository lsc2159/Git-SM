def buy(shopping_bag):
    product = input("[구입]\n상품명? ")
    if product == "":
        return False
    quantity = int(input("수량은? "))
    shopping_bag[product] = quantity
    print(f"장바구니에 {product} {quantity}개가 담겼습니다.")
    return True

def show(shopping_bag):
    print("[장바구니 보기]")
    for product, quantity in shopping_bag.items():
        print(f"{product}: {quantity}")
    print()

def find(shopping_bag):
    product = input("[검색]\n장바구니에서 확인하고자 하는 상품은? ")
    if product in shopping_bag:
        print(f"{product}은(는) {shopping_bag[product]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {product}은(는) 없습니다.")

shopping_bag = {}
while True:
    if not buy(shopping_bag):
        break
    show(shopping_bag)
    find(shopping_bag)






