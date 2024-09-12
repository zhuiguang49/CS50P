def convert():
    str = input ("please enter words!")
    replacement_str1 = str.replace(":)","🙂")
    replacement_str2 = replacement_str1.replace(":(","☹️")
    print(replacement_str2)

def main():
    convert()

main()