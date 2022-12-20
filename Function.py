import random

x = random.randrange(0, 100)

# ----------------------------------------- Funcções -----------------------------------------
def randomSum(y):
    print("Random: ", x)
    print("Resultado: ", x + y)


def inText(string, text):
    if string not in text:
        print("A palavra", string, "não está no texto.")
    else:
        print("A palavra", string, "está no texto.")


def inArray(item, array):
    if item not in array:
        print("O item", item, "não está no array.")
    else:
        print("O item", item, "está no array.")


def listCompress(item, array):
    # sintaxe = [expression for item in iterable if condition == True]
    newList = [x for x in array if item in x]
    return newList


def maior(a=0, b=0):
    if a > b:
        return True
    else:
        return False


def runList(array):
    for item in array:
        print(item)


def listSum(array):
    i = 0
    sum = 0
    while i < len(array):
        sum += array[i]
        i += 1
    return sum


# ------------------------------------------------------------------------------------------------------------------

# ---------------- Soma aleatória ----------------
print("-----------------------------------------------------------------------------")

randomSum(5)

# ---------------- Busca de string ----------------
print("-----------------------------------------------------------------------------")

text = "Um anel para a todos governar, um anel para encontrá-los, um anel para a todos trazer e na escuridão aprisioná-los."
string = "Mordor"
inText(string, text)
text += "Na Terra de Mordor onde as sombras se deitam."
inText(string, text)

# ---------------- Exemplificação do iF e Else ----------------
print("-----------------------------------------------------------------------------")

a = 3
b = 5
if maior(a, b):
    print("A é maior do B")
else:
    print("B é maior do A")

# ---------------- Array ----------------
print("-----------------------------------------------------------------------------")

array = ["banana", "maçã", "pêra", "tomate", "milho", "manga", "morango"]

# ---------------- Ordena o Array ----------------
array.sort()

# ---------------- Operações com Array ----------------
inArray("pêssego", array)
array.append("pêssego")
inArray("pêssego", array)
array.remove("pêssego")
inArray("pêssego", array)
print("Array:", array)
array.pop(3)
print("Remoção do item por indice 3", array)

# ---------------- Compressão do Array ----------------
print("Compressão da lista, somente palavras com letra A:", listCompress("a", array))

# ---------------- Limpeza do Array ----------------
array.clear()
print("Array limpo:", array)

# ---------------- Loop no Array ----------------
print("-----------------------------------------------------------------------------")
array = [1, 5, 10, 20]
array += [25, 15, 55]
array.sort(reverse=True)

print("Array numérico:")
runList(array)
print("Soma de items do array:", listSum(array))
