def quickSort(arr):
    less = []
    pivotList = []
    more = []
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    else:
        pivot = arr[0] # Change this line
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def longestConsecutive(nums):
    if len(nums) <= 1:
        return len(nums)
        #nums = quickSort(nums)
    nums=quickSort(nums)

    maxi = 1
    cur = 1
    for i in range(len(nums)):

        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            cur += 1
        else:
            maxi = max(cur, maxi)
            cur = 1

    return max(cur, maxi)


A=[100,4,200,1,3,2]
print(quickSort(A))
print(longestConsecutive(A))
