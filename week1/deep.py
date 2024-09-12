answer = input("Please enter the answer to the Great Question of Life, the Universe and Everything?")
match answer.strip():
    case "42" | "forty-two" | "Forty-two" | "forty two" | "Forty Two":
        print("yes")
    case _:
        print("No")