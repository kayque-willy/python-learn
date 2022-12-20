def maior(a=0, b=0):
    if a >= b:
        return True
    else:
        return False

name = input("Entre com o nome: ")
print("Seu nome é: " + name)

number = input("Digite um número: ")

if maior(int(number),10):
    print("O número que você digitou é maior ou igual a 10")
else:
    print("O número que você digitou não é maior que 10")