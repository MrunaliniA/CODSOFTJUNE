def add(num1,num2):
	print(num1, "+" ,num2, "=" ,num1+num2)
def sub(num1,num2):
	print(num1, "-" ,num2, "=" ,num1-num2)
def mul(num1,num2):
	print(num1, "X" ,num2, "=" ,num1*num2)
def div(num1,num2):
	print(num1, "/" ,num2, "=" ,num1/num2)
def mod(num1,num2):
	print(num1, "%" ,num2, "=" ,num1%num2)
def sqrt(num1,num2):
	print(num1, "^" ,num2, "=" ,num1**num2)
print("Select Operations:")
print("1.Addition of two numbers \n2.Subtraction of two numbers \n3.Multiplication of two numbers \n4.Division of two numbers \n5.Modulus \n6.Square")
print("************************************************************")
while True:
	operation=(input("Enter Operation : "))
	n1=float(input("Enter First Number : "))
	n2=float(input("Enter Second Number : "))
	print("************************************************************")
	if operation == '1':
		add(n1,n2) 
	elif operation == '2':
		sub(n1,n2)
	elif operation == '3':
		mul(n1,n2)
	elif operation == '4':
		div(n1,n2)
	elif operation == '5':
		mod(n1,n2)
	elif operation == '6':
		sqrt(n1,n2)
	else:
		print("Invalid Operation..........")
	print("************************************************************")
	next=input("Lets do further Calculation (yes/no): ")
	print("############################################################")
	if next == "no":
		break
	elif next == "yes":
		continue
	else:
		print("Value Error...Type 'yes' or 'no'")
		break
