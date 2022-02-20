with open('referat.txt', 'r', encoding='utf-8') as fl:
    for i, value in enumerate(fl):
        read = len(value)
        print(f"Длинна строки {i}: {read} символов")

with open('referat.txt', 'r', encoding='utf-8') as ks:
    result = len(ks.read().split())
    print(f"Количество слов в тексте {result}")

with open('referat.txt', 'r', encoding='utf-8') as lx:
    res = lx.read()
    replace = res.replace('.', '!')
with open('referat2.txt', 'r+', encoding='utf-8') as file:
    file.write(replace)

