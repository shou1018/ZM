def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def longestConsecutive(nums):
        if len(nums) <= 1:
            return len(nums)

        nums = merge_sort(nums)
        #nums.sort()
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

A = [100,4,200,1,3,2]
print(merge_sort(A))
print(longestConsecutive(A))
