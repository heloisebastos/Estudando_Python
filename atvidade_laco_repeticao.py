#recebe um valor e verifica se ele é divisivel pela condições impostas 

# Use uma nomenclatura mais descritiva para variáveis. Por exemplo, "number" em vez de "var".
number = int(input("Digite um valor: "))
var = int (input("digite um valor : "))

cont = 0

while cont <= var :
    if cont % 3== 0 :
        print (str(cont)+" = FIZZ")
    elif cont % 5 == 0 :
        print (str(cont)+" = BUZZ")
    elif (cont % 3 == 0) and (cont % 5 == 0) :
        print (str(cont)+" = FIZZBUZZ")
    else :
        print ("Número " + str(cont) + " não é divisivel por 3 nem 5")
    cont += 1
print ("contagem concluida")

# Use um loop for em vez de um while para iterar sobre os números até o valor fornecido.
# Isso torna o código mais claro e elimina a necessidade de uma variável de contagem separada.
for cont in range(number + 1):
    if cont % 3 == 0 and cont % 5 == 0:
        print(str(cont) + " = FIZZBUZZ")
    elif cont % 3 == 0:
        print(str(cont) + " = FIZZ")
    elif cont % 5 == 0:
        print(str(cont) + " = BUZZ")
    else:
        print("Número " + str(cont) + " não é divisível por 3 nem 5")
