'''
Given an arrary of integers and a target value, return the indices of 2 numbers that add up to the input target value
'''


def two_sum(arr, target):
    num_to_index ={}

    for index, num in enumerate(arr):
        complement = target -num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

    return None

#Example usage:
arr = [2,7,11,15]
target =18
result = two_sum(arr, target)
print(result)