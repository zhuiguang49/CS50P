def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    left_dollar = d.replace("$","")
    result = float(left_dollar)
    return result



def percent_to_float(p):
    temp= p.replace("%","") 
    result = float (temp)/100
    return result


main()