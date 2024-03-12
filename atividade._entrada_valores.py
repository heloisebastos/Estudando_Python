
var = int (input("digite um valor : "))

if var % 3== 0 :
    print ("FIZZ")
elif var % 5 == 0 :
    print ("BUZZ")
elif (var % 3 == 0) and (var % 5 == 0) :
 print ("FIZZBUZZ")
else :
    print ("Número " + str(var) + " nao é divisivel por 3 e 5")