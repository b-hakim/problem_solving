class Solution_1(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ind_start = 0
        curr_sum = nums[0]

        if curr_sum >= target:
            return 1

        found = False
        shortest_length = len(nums)

        for i in range(1, len(nums)):
            curr_sum += nums[i]

            if curr_sum >= target:
                found = True
                l = i - ind_start + 1

                if l == 1:
                    return
                elif l < shortest_length:
                    shortest_length = l

                for j in range(ind_start, i):
                    curr_sum -= nums[ind_start]
                    ind_start += 1

                    if curr_sum >= target:
                        l = i - ind_start + 1

                        if l == 1:
                            return 1
                        elif l < shortest_length:
                            shortest_length = l

                    if curr_sum < target:
                        break

        if not found:
            return 0

        return shortest_length


class Solution(object):
    def binary_search(self, v, arr, i, s, e):
        if s > e or e < s:
            return i
        if s == e:
            return s
        if arr[i] == v:
            return i

        if arr[i] < v:
            new_i = (e - i) // 2 + i
            return self.binary_search(v, arr, new_i, i + 1, e)

        elif arr[i] > v:
            new_i = (i - s) // 2 + s
            return self.binary_search(v, arr, new_i, s, i - 1)

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # binary search solution using cumulative sums

        sums = [0] * (len(nums) + 1)

        for j in range(1, len(nums) + 1):
            sums[j] = sums[j - 1] + nums[j - 1]

        print(sums)
        ans = len(sums)

        for i in range(1, len(sums)):
            sum_find = target + sums[i - 1]
            idx = self.binary_search(sum_find, sums, len(sums)//2, 0, len(sums)-1)

            if idx != len(sums):
                if sums[idx] < sum_find:
                    idx += 1
                if idx != len(sums):
                    ans = min(ans, idx - i + 1)

        return ans if ans != len(sums) else 0


if __name__ == '__main__':
    # print(Solution().minSubArrayLen(6, [2,10, 3]))
    # print(Solution().minSubArrayLen(4, [1,4,4]))
    # print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    # print(Solution().binary_search(6, [0,2,12,15], 2, 0, 4))
    # print(Solution().binary_search(19, [0, 2, 5, 6, 8, 12, 15], 3, 0, 7))
    # print(Solution().binary_search(4, [0, 1, 5, 9], 1, 0, 4))
    print(Solution().binary_search(16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 8, 0, 16))