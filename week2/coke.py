needed = 50
while needed>0:
    print("Amount Due", needed)
    insert = int(input("insert coin:"))
    if(insert == 5 or insert == 10 or insert ==25):
        needed = needed - insert

more = abs(needed)
print("change owed:", more)   