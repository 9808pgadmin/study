# 两数相加，返回数组下标
# class Solution:
#     def sum(self,nums,target):
#         hashmap = {}
#         for index,num in enumerate(nums):
#             num1 = target - num
#             if num1 in hashmap:
#                 return[hashmap[num1]]
#             hashmap[num] = index
#         return(None)
# a = Solution()
# print(a.sum([2,3,4,7,9],9))


# 嵌套使用
def line(char,times):
    """

    :param char: 字符
    :param times: 次数
    """
    print(char * times)
# line("$",10)

def lines(char,time):
    row = 0
    while row<5:
        line(char,time)
        row += 1
lines("#",5)



# 测试[i:j],[i:j:s]
# a=[0,1,2,3,4,5,6,7,8,9]
# b='123pyt123hon'
# c='0123456789'
# print(c[::-2])
# print(b[::-1])
# print(val(b))