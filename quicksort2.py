
def pivot(nums, left, right):
    slow = left
    quick = left
    pivot = nums[right]
    while quick < right:
        if nums[quick] <= pivot:
            nums[slow], nums[quick] = nums[quick], nums[slow]
            slow += 1
        quick += 1
    nums[slow], nums[right] = nums[right], nums[slow]
    return slow

def quicksort(nums, left, right):
    if left < right:
        pi = pivot(nums, left, right)
        quicksort(nums, left, pi-1)
        quicksort(nums, pi+1, right)


def longestConsecutive(nums):
    if len(nums) <= 1:
        return len(nums)
    #quicksort(nums, 0, len(nums)-1)
    maxi = 1
    cur = 1

    for x in nums:
        cur = 1
        print('x =', x)
        y = x
        while y+1 in nums:
            cur += 1
            y += 1
        maxi = max(cur, maxi)
        print(y, cur, maxi)
    return maxi



A=[100,4,200,1,3,2]


print(longestConsecutive(A))
