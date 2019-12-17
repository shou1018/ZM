def TwoSum(nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
       """
       n = len(nums)
       for i in range(0,n):
           for j in range(0,n):
               if (i != j and target - nums[i] == nums[j]):
                   print(i, j)
                   break
