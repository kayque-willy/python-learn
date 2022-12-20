# Exemplo de comentário em python, usa-se o caractere #

print("Hello World!")

# Vaiáveis não precisam ser declaradas com nenhum tipo específico
a = "Olá"
b = 2
c = 2.50
d = False
e = True

print("Variáveis: ", a, b, c, d)
print("Tipos: ", type(a), type(b), type(c), type(d), type(e))

# Outros tipos de dados
# String
x = "Hello World"
# Int
x = 20
# float
x = 20.5
# complex
x = 1j
# list
x = ["apple", "banana", "cherry"]
# tuple
x = ("apple", "banana", "cherry")
# range
x = range(6)
# dict
x = {"name": "John", "age": 36}
# set
x = {"apple", "banana", "cherry"}
# frozenset
x = frozenset({"apple", "banana", "cherry"})
# bool
x = True
# bytes
x = b"Hello"
# bytearray
x = bytearray(5)
# memoryview
x = memoryview(bytes(5))
# NoneType
x = None

# Concatenação de Strings - É possível concatenar as strings com o + no print
a = "Olá "
b = "Mundo "
c = "!"
print("Concatenação de strings: " + a + b + c)

# Operadores matemáticos
a = 1
b = 2

print("Soma: ", a + b)
print("Subtração: ", a - b)
print("Multiplicação: ", a * b)
print("Divisão: ", a / b)

# As variáveis também podem ser atribuidas em linha

a, b, c = "nome 1", "nome 2", "nome 3"
print("Array: ", a, b, c)

# Descompactação - Também é possível atribuir valores do array às variáveis
a, b, c = ["array 1", "array 2", "array 3"]
print("Array descompactação: ", a, b, c)

array = ["Novo array 1", "Novo array 2", "Novo array 3"]
print(array)

# Exibe o intervalo entre o primeiro e o segundo item do array
print("Intervalo Array", array[0:2])

a, b, c = array
print("Novo Array Descompactado: ", a, b, c)
