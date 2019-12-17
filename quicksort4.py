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

nums=[9,1,4,7,3,-1,0,5,8,-1,6]
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

print(max(cur, maxi))



print(longestConsecutive(A))
