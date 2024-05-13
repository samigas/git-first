def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = 3.14 * radius * radius
    return area

print('시작')
radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
result = get_circle_area(radius)
print("원의 넓이는:", result)
print("끝")

