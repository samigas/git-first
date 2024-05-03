shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명?') 
    if len(item) > 0:
        N = int(input('수량은?'))
        print(f' 장바구니에 {item} {N}개 담겼습니다')
        shopping_bag[item] = N
        print()
    else: break

print()
print(f' >>> 장바구니 보기: {shopping_bag}')
print()
print('[검색]')
f_i = input('장바구니에서 확인하고자 하는 상품은?')

if f_i in shopping_bag:
    print(f'{f_i}은(는) {shopping_bag[f_i]}개 담겨있습니다.')
else: print(f'{f_i}는 장바구니에 담겨있지 않습니다')
