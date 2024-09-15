input_str = input("please enter a string:")
result = ""
for i in input_str:
    if i.lower() not in ("a","e","i","o","u"):
        result = result + i
print(result)