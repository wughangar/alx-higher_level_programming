#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    ans = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i]
                num2 = my_list_2[i]
                div = 0
                if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                    try:
                        div = num1 / num2
                        ans.append(div)
                    except (ZeroDivisionError, IndexError) as x:
                        print(x)
                        ans.append(0)
                else:
                    raise TypeError("Wrong type")
            except IndexError:
                print("out of range")
                ans.append(0)
    except (TypeError, IndexError) as x:
        print(x)
        print("An error occured")
    finally:
        return ans

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
