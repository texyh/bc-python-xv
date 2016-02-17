"""def twosum(nums,target):
    index_list = range(len(nums))
    for idx in index_list:
        ist_num = nums[idx]
        for idx_j in range(idx+1,len(nums)):
            sec_num = nums[idx_j]
            num_sum = ist_num + sec_num
            if target == num_sum:
                #print (idx,idx_j)
                
                return [idx,idx_j]"""
            

   #pass
def twosum(nums,target):
    dict_hold = {}
    for idx in nums:
        tar = target - idx
        if tar in dict_hold:
            #print ([dict_hold[tar],nums.index(idx)])
            return [dict_hold[tar],nums.index(idx)]
        else:
            dict_hold[idx] = nums.index(idx)
twosum([1,2,3,5],8)
