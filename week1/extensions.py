def category(n):
    if n.endswith(".gif"):
        print(".gif")
    elif n.endswith(".jpg"):
        print(".jpg")
    elif n.endswith(".jpeg"):
        print(".jpeg")
    elif n.endswith(".png"):
        print(".png")
    elif n.endswith(".pdf"):
        print(".pdf")
    elif n.endswith(".txt"):
        print("txt")
    elif n.endswith(".zip"):
        print(".zip")

name = input("Please enter a file name").lower()

category(name)