def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(price):
    n500 = price//500
    n100 = (price%500)//100
    n50 = ((price%500)%100)//50
    n10 = (((price%500)%100)%50)//10
    print('500원 짜리는:', n500, '개', '100원 짜리는:', n100, '개', '50원 짜리는:', n50, '개', '10원짜리는:', n10, '개이다')

pri = int(get_integer('동전으로 바꾸고 싶은 금액은?'))
result= exchange(pri)
print(result)
