direction = input("Шифрование или дешифрование: ш/д \n")

alphabet = input("Английский или русский: а/р \n")

step = int(input("Шаг сдвига: "))

text= input("Введите текст: ")

def caesar(direction,alphabet,step,text):
    eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_upper_alphabet ="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    rus_lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if alphabet == "р":
        if direction == "д":
            for i in text:
                if i in rus_lower_alphabet:
                    ind = rus_lower_alphabet.index(i)
                    new_i = rus_lower_alphabet[ind-step]
                    print(new_i, end ="")
                elif i not in (rus_lower_alphabet and rus_upper_alphabet):
                    print(i,end="")
                else:
                    ind = rus_upper_alphabet.index(i)
                    new_i = rus_upper_alphabet[ind - step]
                    print(new_i, end="")
        else:
            for i in text:
                if i in rus_lower_alphabet:
                    ind = rus_lower_alphabet.index(i)
                    if ind + step > 33:
                        new_i = 33 - ind
                        new_i = step - new_i
                        print(rus_lower_alphabet[new_i-1], end="")
                    else:
                        new_i = rus_lower_alphabet[(ind+step)]
                        print(new_i, end ="")
                elif i not in (rus_lower_alphabet and rus_upper_alphabet):
                    print(i, end="")
                else:
                    ind = rus_upper_alphabet.index(i)
                    if ind + step > 33:
                        new_i = 33 - ind
                        new_i = step - new_i
                        print(rus_upper_alphabet[new_i-1], end="")
                    else:
                        new_i = rus_upper_alphabet[(ind+step)]
                        print(new_i, end ="")
    else:
        if direction == "д":
            for i in text:
                if i in eng_lower_alphabet:
                    ind = eng_lower_alphabet.index(i)
                    new_i = eng_lower_alphabet[ind-step]
                    print(new_i, end ="")
                elif i not in (eng_lower_alphabet and eng_upper_alphabet):
                    print(i, end="")
                else:
                    ind = eng_upper_alphabet.index(i)
                    new_i = eng_upper_alphabet[ind - step]
                    print(new_i, end="")
        else:
            for i in text:
                if i in eng_lower_alphabet:
                    ind = eng_lower_alphabet.index(i)
                    if ind + step > 25:
                        new_i = 25 - ind
                        new_i = step - new_i
                        print(eng_lower_alphabet[new_i-1], end="")
                    else:
                        new_i = eng_lower_alphabet[(ind+step)]
                        print(new_i, end ="")
                elif i not in (eng_lower_alphabet and eng_upper_alphabet):
                    print(i, end="")
                else:
                    ind = eng_upper_alphabet.index(i)
                    if ind + step > 25:
                        new_i = 25 - ind
                        new_i = step - new_i
                        print(eng_upper_alphabet[new_i-1], end="")
                    else:
                        new_i = eng_upper_alphabet[(ind + step)]
                        print(new_i, end="")

print(caesar(direction,alphabet,step,text))