print("Sol. will start here.")

a = 30 
b = 50
c = a + b
d = c * 2  # (30 + 50) * 2 = 160
e = b - a
f = e * 2  # (50 - 30) * 2 = 40

# Fixed: Changed '=' to '=='
if (d == f):
    print("The equation is balanced with specific variables.")
else:
    print("The equation is not balanced with specific variables.")

# Fixed: Added 'elif' to handle if they are equal
if (d > f):
    print("Var D is greater than F")
elif (f > d):
    print("Var F is greater than D")
else:
    print("Var D and Var F are equal")

# Fixed: Corrected the typo 'accespt' to 'accept'
print("This is the solution to your answer")
print("May you accept this.")
