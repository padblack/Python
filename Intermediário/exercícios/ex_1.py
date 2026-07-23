#Multiplicar argumentos não nomeados
def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

number = map(int, input().split())
multiplication = multiply(*number)
 
print(multiplication)

#Ver se um número é par ou ímpar
def pair_or_odd(x):
    if (x % 2) == 0:
        return "pair"
    else:
        return "odd"

number = int(input())
print(pair_or_odd(number))