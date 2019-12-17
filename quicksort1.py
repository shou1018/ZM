def pivot_swap(nums, left, right):
    slow = left
    quick = left
    pivot = nums[right]
    while quick < right:
        print(left, right, slow, quick, nums[slow], nums[quick], nums[right], '--', nums)
        if nums[quick] <= pivot:
            nums[slow], nums[quick] = nums[quick], nums[slow]
            slow += 1
        quick += 1
    print(left, right, slow, quick, nums[slow], nums[quick], nums[right], '--', nums)

    nums[slow], nums[right] = nums[right], nums[slow]
    print('New Pivot------', slow, nums)
    return slow

def quick_sort(nums, left, right):
    if left < right:
        pi = pivot_swap(nums, left, right)
        quick_sort(nums, left, pi-1)
        quick_sort(nums, pi+1, right)


A=[9,1,4,7,3,-1,0,5,8,-1,6]

quick_sort(A, 0, 10)
print(A)
