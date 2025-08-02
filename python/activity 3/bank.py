greeting = input("Want 100 bucks? Just greet us. ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")