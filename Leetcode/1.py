'''
Given an array of integers, write a function to move all 0's to the end while maintaining the relative order of the other elements
'''

def move_zeros(arr):
    non_zero_element = [num for num in arr if num != 0]
    zero_count = len(arr) -len(non_zero_element)
    return non_zero_element + [0]*zero_count

#Example usage:
arr = [0,1,0,3,12]
result = move_zeros(arr)
print(result)