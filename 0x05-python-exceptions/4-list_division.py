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
                    except ZeroDivisionError:
                        print("division by 0")
                        ans.append(0)
                    else:
                        ans.append(div)
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
