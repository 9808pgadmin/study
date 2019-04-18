class solution():
    def sum(self,nums,target):
        hash ={}
        for index,num in enumerate(nums):
            num1 = target-num
            if num1 in hash:
                return [hash[num1],index]
            hash[num] = index
        return None
a= solution()
print(a.sum([1,2,3,4,7,6],8))