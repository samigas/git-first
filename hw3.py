discount_rate = 0

rate = int(input('할인률은?'))

def set_rate(rate) :
    global discount_rate
    discount_rate = rate

def get_fixed_price(price) :
    cost = (price / (1-(rate/100)))
    return cost
    

discount_priceA = int(input('A상품의 할인된 가격은?'))
discount_priceB = int(input('B상품의 할인된 가격은?'))

costA = get_fixed_price(discount_priceA)
costB = get_fixed_price(discount_priceB)

print('A상품의 정가는', costA)
print('B상품의 정가는', costB)
