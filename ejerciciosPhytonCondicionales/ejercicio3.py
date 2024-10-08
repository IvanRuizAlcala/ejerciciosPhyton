num1 =input("dime un numero: ")
num2 =input("dime otr numero: ")
if num1.isnumeric() and num2.isnumeric() :
    total = num1 /num2
if num2<=0 :
    input(" error ")
else:
    input(total)