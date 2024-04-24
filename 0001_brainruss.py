# Часть кода скопирована
def block(code: str) -> object:
    opened = []
    blocks = {}
    for i in range(len(code)):
        if code[i] == '[':
            opened.append(i)
        elif code[i] == ']':
            blocks[i] = opened[-1]
            blocks[opened.pop()] = i
    return blocks

def parse(code: str) -> str:
    return ''.join(c for c in code if c in '><+-.,[]')

def run(code: str) -> None:
    code = parse(code)
    x = i = 0
    bf = {0: 0}
    blocks = block(code)
    l = len(code)
    while i < l:
        sym = code[i]
        if sym == '>':
            x += 1
            bf.setdefault(x, 0)
        elif sym == '<':
            x -= 1
        elif sym == '+':
            bf[x] += 1
        elif sym == '-':
            bf[x] -= 1
        elif sym == '.':
            print(chr(bf[x]), end='')
        elif sym == ',':
            bf[x] = int(input('Input: '))
        elif sym == '[':
            if not bf[x]: i = blocks[i]
        elif sym == ']':
            if bf[x]: i = blocks[i]
        i += 1

# А часть - нет
def convert(code: str, invert=False) -> str:
    copyCode = code
    symbols = "><+-.,[]"
    description = ["СледующаяЯчейка", "ПредыдущаяЯчейка", 
                   "УвеличитьЯчейкуНа1", "УменьшитьЯчейкуНа1",
                   "ВыводЯчейки", "ВводЯчейки",
                   "НачалоЦикла", "КонецЦикла"
                   ]
    if invert:
        for i in range(len(symbols)):
            copyCode = copyCode.replace(symbols[i], description[i])
        return copyCode
    
    for i in range(len(symbols)):
        copyCode = copyCode.replace(description[i], symbols[i])
    return copyCode

# Для примера
example = ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>+.>++++++++++."
print(convert(example, invert=True), "\n-------------")

code = input()
print("\nРезультат:")
run(convert(code))