#Selection sort
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort_desc(arr)
print(sorted_arr)



#Bubble sort

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = bubble_sort_desc(arr)
print(sorted_arr) # Output: [64, 25, 22, 12, 11]



#insertion sort
def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = insertion_sort_desc(arr)
print(sorted_arr) # Output: [64, 25, 22, 12, 11]



#Merge sort
def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [64, 25, 12, 22, 11]
sorted_arr = merge_sort_desc(arr)
print(sorted_arr) # Output: [64, 25, 22, 12, 11]
