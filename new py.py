# print ("hi")
# print(5+5)
# print(5-5)
# print(5*5)
# print(5/5)
# print(5%2)
# print(2**10)

# print('-'*100) 

# print(5 == 5)

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a <= b + c:
    if c <= a + b:
        if b  <= a + c:
            print('tak!')
        else:
            print('nie!')
    else:
        print('nie!')
else:
    print('nie!')            