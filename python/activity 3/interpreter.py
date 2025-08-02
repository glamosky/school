expression = input("Expression (DO NOT FORGET SPACES): ")  # User types: "1 + 1"
parts = expression.split(" ")       # Splits into: ["1", "+", "1"]

x = int(parts[0])      
y = parts[1]           
z = int(parts[2])

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(x / z)
