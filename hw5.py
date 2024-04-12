def read_single_digit(Num):
    if Num == '1':
        return '일'
    elif Num == '2':
        return '이'
    elif Num == '3':
        return '삼'
    elif Num == '4':
        return '사'
    elif Num == '5':
        return '오'
    elif Num == '6':
        return '육'
    elif Num == '7':
        return '칠'
    elif Num == '8':
        return '팔'
    elif Num == '9':
        return '구'
    else:
        return '영'

number = input('세자리 정수를 입력하세요')

def read_number(num):
    X = read_single_digit(num[0:1])
    Y = read_single_digit(num[1:2])
    Z = read_single_digit(num[2:3])
    T = X + Y + Z
    return T

Rnum = read_number(number)
print(f'{Rnum}')
