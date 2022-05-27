# How can you make this more scalable and reusable later?
import functools
def find_armstrong_numbers(numbers):
    base_list = []
    ans_list = []
    for x in numbers:
        if len(str(x)) == 1:
            base_list.append(x)
        elif len(str(x)) == 2:
            lis = list(map(int,str(x)))
            lis2 = list(map(lambda item : item ** 2, lis))
            lis3 = functools.reduce(lambda agg, item : agg + item, lis2)
            base_list.append(lis3)
        elif len(str(x)) == 3:
            lis = list(map(int,str(x)))
            lis2 = list(map(lambda item : item ** 3, lis))
            lis3 = functools.reduce(lambda agg, item : agg + item, lis2)
            base_list.append(lis3)
    for x in range(0, len(numbers), 1):
        if numbers[x] == base_list[x]:
            ans_list.append(numbers[x])
    return ans_list

