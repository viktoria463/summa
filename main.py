def countNumbers(v): 
 summa = 0
 for simbols in v:
    summa = summa + int(simbols)
 return summa
v = input("Ievadi skaitli: ")
rez = countNumbers(v)
print("Summa ir ", rez)
