name = input("please enter name of variable in camel case")
name_list = list(name)

converted_name = []

for i in name_list:
    if i.isupper():
        converted_name.append("_"+i.lower())
    else:
        converted_name.append(i)

print (''.join(converted_name).lstrip("_"))