#Swap Two Number
a=int(input("Enter the Fast Number:"))
b=int(input("Enter the second Number:"))


print(f"Before a={a} Swap b={b} and ")

a=a^b
b=a^b
a=a^b

print(f"After Swap a={a} and b={b}")