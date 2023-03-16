def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(r):
    area = r*r*3.14
    print('반지름'+str(r)+'인 원의 넓이='+'3.14*'+str(r)+'*'+str(r)+'='+str(area))

r=get_radius("넓이를 구하고자 하는 원의 반지름은?")
get_circle_area(r)
