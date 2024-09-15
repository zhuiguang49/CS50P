def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    '''
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            flag = 1
            for i in range(s):
                if (i.isalpha() == false) and (i.isdigit() == false):
                    flag = 0
                
            if flag == 1:
                for i in range(s):
                    if i.isdigit():
                        if i ==0:
                            return false
                        else:
                            break
                #要求数字在中间的部分不知道该怎么实现，所以空着了

    return false
    '''
    #这是让ChatGPT帮忙实现的一个版本
    # 所有车牌必须至少以两个字母开头
    if not s[:2].isalpha():
        return False

    # 车牌最多可包含 6 个字符（字母或数字），最少包含 2 个字符
    if not 2 <= len(s) <= 6:
        return False

    # 检查数字是否在中间
    for char in s[2:-1]:
        if char.isdigit():
            return False

    # 检查最后是否有数字，且第一个数字不能是 0
    found_digit = False
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            if s[i] == '0' and not found_digit:
                return False
            found_digit = True

    # 不允许有句号、空格或标点符号
    if not s.isalnum():
        return False

    return True

main()