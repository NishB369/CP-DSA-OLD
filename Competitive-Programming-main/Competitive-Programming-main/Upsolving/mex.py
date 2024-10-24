def mex(nums):
    nums_set = set(nums)
    mex_num = 0
    while mex_num in nums_set:
        mex_num += 1
    return mex_num
print(mex([0,1,2,5,7,8]))