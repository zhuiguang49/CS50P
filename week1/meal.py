def main():
    time = convert(input("Please input meal time!"))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time=time.split(sep=":")
    total=float(time[0])+float(time[1])/60
    return total

if __name__ == "__main__":
    main()