n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
try:
	result = n1 / n2
	print("Result:", result)
except:
	print("Error: Cannot divide by zero.")
finally:
	print("Completed Execution")