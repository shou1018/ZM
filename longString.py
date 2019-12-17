def LongString(A):
    A=set(A)
    maxi = 1
    for i in A:
        cur = 1
        while i + 1 in A:
            cur += 1
            i += 1
        maxi = max(maxi,cur)
    return maxi





nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(LongString(nums))
