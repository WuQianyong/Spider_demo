# encoding:utf-8


"""
一些算法提
"""

"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        else:
            data_dict = {}
            for i, num in enumerate(nums):
                if num not in data_dict.keys():
                    data_dict[num] = [i]
                else:
                    data_dict[num].append(i)
            for one in sorted(data_dict.keys()):
                if target - one in data_dict.keys():
                    if one == target - one:
                        return data_dict.get(one)
                    else:
                        return [data_dict.get(one)[0], data_dict.get(target - one)[0]]

    def add_two_num(self, l1, l2):
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next
        :param l1:
        :param l2:
        :return:
        """
        if len(l1) == len(l2):
            new_list = []
            for i in range(len(l1)):
                if len(new_list) < i + 1:
                    if l1[i] + l2[i] < 10:
                        new_list.append(l1[i] + l2[i])
                    else:
                        new_list.append(l1[i] + l2[i] - 10)
                        new_list.append(1)
                else:
                    new_list[i] = new_list[i] + l1[i] + l2[i]
            return new_list


        else:
            return False

    def find_substring(self, s):
        """
        寻找字符串里面的不重复字符
        :param s:
        :return:
        """
        # s_len = len(s)
        # sub_s
        # for i in range(s_len):
        alive = True
        while alive:
            print('I Love My Goddesses')

        # for (i=0,i<100,i++):

if __name__ == '__main__':
    demo = Solution()

    # two num
    # nums = [2,3,3,4]
    # target = 6
    # nums = [3, 2, 4]
    # print(demo.twoSum(nums, target))

    # add two num
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    # print(demo.add_two_num(l1, l2))

    s = 'pwwkew'
    demo.find_substring(s)
