#Sets the values for calculator to use
val1 = int(input ("Enter the first value: "))
val2 = int(input ("Enter the second value: "))

#Asks what operation to use
print ("1. Add")
print ("2. Subtract")
print ("3. Divide")
print ("4. Multiply")
op = input ("What operation should I use:")

#Addition
if op == '1':
    print(val1, " + ", val2, " = ", (val1 + val2))

#Subtraction
elif op == '2':
    print(val1, " - ", val2, " = ", (val1 - val2))

#Division
elif op == '3':
    print(val1, " / ", val2, " = ", (val1 / val2))

#Multiplication
elif op == '4':
    print(val1, " * ", val2, " = ", (val1 * val2))
