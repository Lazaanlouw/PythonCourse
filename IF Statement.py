# is_male = False
# is_tall = False
#
# if is_male & is_tall:
#     print("You are Male and you are tall")
# elif is_male and not is_tall:
#     print("You are Male, but you not tall")
# elif not is_male and is_tall:
#     print("You are not a Male, but you are tall")
# else:
#     print("You are neither of the two")

#
# if is_male or is_tall:
#     print("You are Male or you are tall or both")
# else:
#     print("You neither male or tall")

# if not is_male & is_tall:
#     print("You are a Woman")
# else:
#     print("You are a Niggah")


def highest_num(num1, num2, num3):
    if num1 >= num2 & num1 >= num3:
        return num1
    elif num1 <= num2 & num2 >= num3:
        return num2
    else:
        return num3


print(highest_num(3, 10, 6))
