class Solution:
    def addTwoNumbwes(self,l1,l2):
        num1_str = ""
        num2_str = ""
        while l1 or l2:
            if l1:
                num1_str=num1_str+str(l1.val)
                l1=l1.next
            if l2:
                num2_str=num2_str+str(l2.val)
                l2=l2.next
        num1 = int(num1_str[::-1])
        num2 = int(num2_str[::-1])
        sum_num=num1+num2
        next_node = None
        for one in str(sum_num):
            one_int = int(one)
            ln = ListNode(one_int)
            ln.next=next_node
            next_node = ln
        return ln
a=Solution()
print(a.addTwoNumbwes([2,4,5],[5,6,4]))