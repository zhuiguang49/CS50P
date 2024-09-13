def calculate(x,y,z):
    x=float(x)
    z=float(z)
    if y == '+' :
        print(round(float(x+z),1))
    elif y == '-':
        print(round(float(x-z),1))
    elif y == '*':
        print(round(float(x*z),1))
    elif y == '/' and z != 0:
        print(round(float(x/z),1))

expression = input("please enter a calculation expression!").split(sep=" ")
list_e = list(expression)
calculate(list_e[0],list_e[1],list_e[2])

