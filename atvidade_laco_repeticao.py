#recebe um valor e verifica se ele é divisivel pela condições impostas 

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
