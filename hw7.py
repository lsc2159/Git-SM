shopping_bag = []
while True:
    item = input("상품명? ")
    if item == "":
        break
    gets= int(input('수량은?'))
    shopping_bag.append(item)
    shopping_bag[item]=int(gets)
    print(f"장바구니에 {item}가(이) {gets}개가 담겼습니다.")

print(f"\n장바구니 보기: {shopping_bag}")

look_item=input('장바구니에서 확인하고자 하는 상품은? ')
if look_item in shopping_bag:
    print(f"{look_item}은(는) {shopping_bag[look_item]}개 ")
