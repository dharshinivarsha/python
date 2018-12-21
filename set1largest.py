Num1=10
Num2=14
Num3=15
if (Num1 >= Num2) and (Num1 >= Num3):
   largest = Num1
elif (Num2 >= Num1) and (Num2 >= Num3):
   largest = Num2
else:
   largest = Num3

print("The largest number between",Num1,",",Num2,"and",Num3,"is",largest)
