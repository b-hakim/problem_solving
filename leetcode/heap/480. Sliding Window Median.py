import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        lower, higher = [], []

        def get_median():
            if len(lower) == len(higher):
                return (lower[0] * -1 + higher[0]) / 2
            if len(lower) > len(higher):
                return lower[0] * -1
            return higher[0]

        def balance_heaps():
            if lower and higher:
                if lower[0] * -1 > higher[0]:
                    heapq.heappush(higher, heapq.heappop(lower) * -1)
            if len(lower) > len(higher) + 1:
                heapq.heappush(higher, heapq.heappop(lower) * -1)
            if len(higher) > len(lower) + 1:
                heapq.heappush(lower, -1 * heapq.heappop(higher))

        def add_num_to_heaps(num):
            heapq.heappush(lower, -1 * num)
            balance_heaps()

        def remove_num_from_heap(num):
            if lower[0] * -1 >= num:
                # print("lower", lower, "higher", higher, "num*-1", num*-1)
                lower.remove(num * -1)
                heapq.heapify(lower)
            else:
                higher.remove(num)
                heapq.heapify(higher)

            balance_heaps()

        # initialization of the heaps
        for num in nums[0:k]:
            add_num_to_heaps(num)

        medians.append(get_median())

        # looping through nums
        for i in range(k, len(nums)):
            print(nums[i - k])
            remove_num_from_heap(nums[i - k])
            add_num_to_heaps(nums[i])
            medians.append(get_median())

        return medians


