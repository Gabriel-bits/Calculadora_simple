import time

n1 = int(input("escreva um numero "))

m1 = int(input("qual e o multiplo "))

print(n1)
while n1 < 100:
    r1 = n1 + m1
    print(r1)
    n1 = r1
    time.sleep(0.1)

    if n1 >= 100:
        break

print('ta pronto')