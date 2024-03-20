import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ""

count = int(input("Укажите количество паролей для генерации: "))
len_pw = int(input("Укажите длину одного пароля: "))
num = input("Включать ли цифры в пароль? ")
ABC_pw =  input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
abc_pw = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
ch_pw = input('Включать ли символы !#$%&*+-=?@^_? ')


if num.lower() == "да":
    chars += digits
if ABC_pw.lower() == "да":
    chars += uppercase_letters
if abc_pw.lower() == "да":
    chars += lowercase_letters
if ch_pw.lower() == "да":
    chars +=punctuation



def generate_password(len_pw,chars):
    password = ""
    for i in range(len_pw):
        password += random.choice(chars)
    return password

for _ in range(count):
    print(generate_password(len_pw, chars))











