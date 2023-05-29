#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    ans = []
    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i]
                num2 = my_list_2[i]
                div = 0
                if isinstance(num1, (inr, float)) and isinstance(num2, (int, float)):
                    try:
                        div = num1 / num2
                    except ZeroDivisionError:
                        print("division by 0")
                    else:
                        ans.append(div)
                else:
                        print("wrong type")
            except IndexError:
                print("out of range")
                ans.append(0)
    except Exception:
        print("An error occured")
    finally:
        return ans
