greeting = input("enter your greeting words!")
input_str = greeting.strip().lower()
if input_str.startswith("hello") :
    print("$0")
elif input_str.startswith("h") :
    print("$20")
else:
    print("$100")