def buy(S):
    a = input("상품명?")
    if len(a) > 0 :
        b = input("수량은?")
        S[a] = b
    else :
        return False

def show(B) :
    print(B)

def find(SB) :
    F_P = input("장바구니에 확인하고자 하는 상품은?")
    if F_P in SB :
        print(f'장바구니에 {F_P}(는) {SB[F_P]}개 담겨있습니다')
    else :
        print(f'장바구니에 {F_P}은(는) 없습니다')




shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
