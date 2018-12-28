print("Enter 'X' for exit.");
num = input("Enter any number: ");
if num == 'X':
    exit();
try:
    number = float(num);
except ValueError:
    print(" enter a number...");
else:
    check = number%2;
    if check == 0:
    	    print(int(number), "is an EVEN number.");
    elif check == 1:
    	print(int(number), "is an ODD number.");
    else:
    	print(number, "is strange.");
