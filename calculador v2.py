import time

m1 = input('qual e o estilo da conta ? ')

if m1 == '%':
    n1 = int(input("qual tabela vc que ? "))

    n2 = int(input("qual numero começa essa tabela ? "))

elif m1 == '*':
    n1 = int(input('qual numero vc que multiplica ? '))

    n2 = int(input('O multiplo ? '))

elif m1 == '/':
    n1 = int(input("qual o numero ? "))

    n2 = int(input("qual o divisor ? "))


if m1 == '%':
    print(n1)
    while n1 < 100:
        r1 = n1 + n2
        print(r1)
        n1 = r1
        time.sleep(0.01)

        if n1 >= 100:
            break

    print('ta pronto')

elif m1 == '*':
    r1 = n1 * n2
    print(r1)

elif m1 == '/':
    r1 = n1 // n2
    print(r1)

    print('===[ ta pronto ]===')
#elif m1 == '//':

#elif m1 == '%':
#    while n1 :


#print('ta pronto')
