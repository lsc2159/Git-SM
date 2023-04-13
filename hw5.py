def read_number(n):
    d1=n%10
    n//=10
    d10=n%10
    n//=10
    read_single_digit(n)
    read_single_digit(d10)
    read_single_digit(d1)

def read_single_digit(n):
    if n==0: print('영', end=' ')
    elif n==1: print('일', end=' ')
    elif n==2: print('이', end=' ')
    elif n==3: print('삼', end=' ')
    elif n==4: print('사', end=' ')
    elif n==5: print('오', end=' ')
    elif n==6: print('육', end=' ')
    elif n==7: print('칠', end=' ')
    elif n==8: print('팔', end=' ')
    elif n==9: print('구', end=' ')

num=int(input('세 자리 정수 입력: '))
read_number(num)