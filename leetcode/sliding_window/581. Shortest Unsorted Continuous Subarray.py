class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_index = -1
        end_index = -1
        length = -1

        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[1] >= nums[0] else 2

        for i in range(1, len(nums)):
            if start_index == -1:
                if nums[i] <= nums[i - 1]:
                    start_index = i - 1
                    end_index = i
                    sub_list_max = nums[i - 1]
            else:
                if (nums[i] <= nums[i - 1] and nums[i] != sub_list_max) or nums[i] < sub_list_max:
                    end_index = i
                    if nums[i] > sub_list_max:
                        sub_list_max = nums[i]
                # else:
                # if length == -1:
                length = end_index - start_index + 1
                # else:
                # new_length = end_index - start_index + 1
                # if new_length < length:
                #     length = new_length

                # start_index, end_index = 0, 0

        if start_index == -1 or end_index == -1:
            return 0

        if nums[start_index] == nums[end_index]:
            return 0

        return end_index - start_index + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([1,2,3,3,3]))
    # print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))