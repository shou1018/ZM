A = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
#A = [[1,3,5]]
m = len(A)
n = len(A[0])
start = 0;
end = m*n
target = 13

x = False
while start < end:
    mid = (start+end)//2
    mid_r = mid // n
    mid_c = mid % n
    print(start, mid, end, A[mid_r][mid_c] )
    if A[mid_r][mid_c] == target:
        x = True
        break
    elif A[mid_r][mid_c] < target:
        start = mid + 1
    else:
        end = mid



print(x)
