def iplus(x1,x2):
    isum = x1 + x2
    print(isum)
    return isum #return이 output이다.
hap = iplus(4,5)
print(hap)

def print_star():
    print('***')
a = print_star()
print(a) # output이 없음.

def root(a,b,c):
    D = b**2.0 - 4.0*a*c
    if D<0:
        print('해가 없습니다.')
        return None
    x1 = (-b + D)/(2.0*a)
    x2 = (-b - D)/(2.0*a)
    return x1,x2

r1 = root(1,2,1)
print(r1)
r2 = root(1,2,3)
print(r2)


# if type(r1) == complex: print('허수')도 가능.

def print_sum():
    a = 1
    b = 2
    result = a+b
    print('print_sum() 내부:', a,'과',b,'의 합은',result,'입니다')

a = 10
b = 20
print_sum()
result = a+b
print('print_sum() 외부:',a,'과',b,'의 합은',result,'입니다')

#함수 내에 지역변수가 있으면 지역변수를 사용하고, 아니면 전역변수를 사용한다. 
