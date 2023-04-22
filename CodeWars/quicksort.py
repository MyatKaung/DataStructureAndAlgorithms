def quicksort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    left =[x for x in arr if x<pivot]
    right =[x for x in arr if x>pivot]
    middle =[x for x in arr if x==pivot]
    return quicksort(left)+middle+quicksort(right)

array = [3,6,8,10,1,2,1]
print(quicksort(array))
'''
[3,6,8,10,1,2,1]

pivot:10

left:[3,6,8,1,2,1]
right:[]
middle:[10]

[10,3,6,8,1,2,1]

pivot:1
left:[]
right:[3,6,8,2]
middle:[1,1]
[1,1,3,6,8,2,10]


'''

