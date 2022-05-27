# How can you make this more scalable and reusable later?
import functools
def find_armstrong_numbers(numbers):
    #creating a base list to initially append the skipped over and modified numbers into in order
    base_list = []
    #ans list to push the matching values into
    ans_list = []
    #for loop to iterate through the given array
    for x in numbers:
        #single digits should all pass so just appending them
        if len(str(x)) == 1:
            base_list.append(x)
            #else need to split the num and take each digit to power of length
        else:
            #storing the split num list under lis
            lis = list(map(int,str(x)))
            #taking value at each index to power of the length and storing under lis2
            lis2 = list(map(lambda item : item ** len(lis), lis))
            #reducing the split num products and appending to the base list
            lis3 = functools.reduce(lambda agg, item : agg + item, lis2)
            base_list.append(lis3)
    #for loop matching the index count in the arrays to loop through and compare index to index
    #if they match they are an armstrong and appending them to the ans list then returning the fina list
    for x in range(0, len(numbers), 1):
        if numbers[x] == base_list[x]:
            ans_list.append(numbers[x])
    return ans_list

