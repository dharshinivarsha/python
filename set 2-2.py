num=input("enter any number :")
try:
val=int(num)
if num==str(num)[::-1]:
print('the given number is palindrome')
else:
print('the given number is not a  palindrome')
except valueerror:
print("that's not a valid number,try again!")
