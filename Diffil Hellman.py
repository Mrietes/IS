
from sympy import isprime, totient, factorint

def primitive_root(p):

    if not isprime(p):
        print(f"Число {p} не является простым.")
        return False

    phi = totient(p) #Функция Эйлера определяет количество целый чисел от 1 до -1, которые взаимно просты с p
    phi_factors = factorint(phi) #Нахождение простых делителей
    for g in range(1, p+1):
        check = True #Удовлетворяет ли g условиям первообразного корня
        for i in phi_factors: #Перебор всех простых делителей
            check &= pow(int(g), int(phi//i), p) != 1 #g в степени phi деленное нат каждый простой делитель i  по модулю равен p не равно 1
        if check:
            return g

p = int(input("Введите простое число p: "))
g = primitive_root(p)

alice = int(input("Секретный ключ Алисы: "))
robert = int(input("Секретный ключ Боба: "))

a = pow(g,alice,p) #Вычисление открытого ключа Алисы
print(f"Открытый ключ Алисы: {a}. ")

b = pow(g,robert,p) #Вычисление открытого ключа Боба
print(f"Открытый ключ Боба {b}. ")

# Алиса и Боб обмениваются открытыми ключами и вычисляют общий секретный ключ
shared_secret_Alice = pow(b, alice, p)
shared_secret_Robert = pow(a, robert, p)

print("Общий секретный ключ для Алисы:", shared_secret_Alice)
print("Общий секретный ключ для Боба:", shared_secret_Robert)

result = primitive_root(p)
if result:
    print(f"Первообразный корень по модулю {p}: {result}")
else:
    print(f"Для числа {p} не найден первообразный корень.")










