
def pivot(nums, left, right):
    print('pivot once')
    i = left - 1
    j = right + 1
    print('1:', i,j)
    mid = (left + right) // 2
    pivot = nums[mid]
    while True:
        while True:
            i = i + 1
            print('while i:',i)
            if nums[i] < pivot:
                continue
            else:
                break
        while True:
            j = j - 1
            print('while j:',j)
            if nums[j] > pivot:
                continue
            else:
                break
        if i >= j:
            print('2:', i,j)
            return j
        print('before:', nums)
        nums[i], nums[j] = nums[j], nums[i]
        print('after:', nums)

def quicksort(nums, left, right):
    if left < right:
        pi = pivot(nums, left, right)
        quicksort(nums, left, pi)
        quicksort(nums, pi+1, right)


def longestConsecutive(nums):
    if len(nums) <= 1:
        return len(nums)
        #nums = quickSort(nums)
    quicksort(nums, 0, len(nums)-1)

    maxi = 1
    cur = 1
    for i in range(1, len(nums)):

        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            cur += 1
        else:
            maxi = max(cur, maxi)
            cur = 1

    return max(cur, maxi)




A=[2, 0, 1, 0]

#print(quicksort(A, 0, len(A)-1))
print(longestConsecutive(A))
