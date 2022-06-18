import heapq
from typing import List


class Solution1_DP:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mask = 0
        self.profits = profits
        self.capital = capital
        self.max_tasks = 2**len(self.profits)
        return self.solve(0, k, w) + w

    def set_bit(self, mask, bit):
        mask |= 1 << bit
        return mask

    def solve(self, mask, k, w):
        if k == 0 or mask == self.max_tasks - 1:
            return 0

        max_profit = 0

        for i in range(len(self.profits)):
            taken = (mask & (1 << i))>>i == 1
            if self.capital[i] <= w and not taken:
                f = True
                bbit = self.set_bit(mask, i)
                # print(mask, bbit)
                tmp = self.solve(bbit, k - 1, w + self.profits[i]) + self.profits[i]

                if tmp > max_profit:
                    max_profit = tmp

        return max_profit


class Solution_without_heap:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        visited = 0
        self.profits = profits
        self.capital = capital

        # greedy solution
        # 1. find the maximum profit for available projects (a. not taken b. capital <= current_capital
        # 2. Do that project: a. add the profit to w  b. mark it as visited

        for i in range(k):
            max_prof = -1
            max_i = -1

            for project_i in range(len(self.capital)):
                # check if project is available
                if self.get_bit(visited, project_i) == 0 and self.capital[project_i] <= w:
                    if max_prof < self.profits[project_i]:
                        max_prof = self.profits[project_i]
                        max_i = project_i

            if max_prof == -1:
                return w

            w += self.profits[max_i]
            visited = self.set_bit(visited, max_i)

        return w

    def set_bit(self, mask, bit):
        mask |= 1 << bit
        return mask

    def get_bit(self, mask, bit):
        return (mask & (1 << bit)) >> bit


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        visited = 0
        self.profits = profits
        self.capital = capital
        cap_profit_heap = list(zip(self.capital, self.profits))
        heapq.heapify(cap_profit_heap)

        # greedy solution + Heap for maximum available profit
        # 1. find the "maximum profit" for available projects (a. not taken b. capital <= current_capital
        # 2. Do that project: a. add the profit to w  b. mark it as visited

        available_projects_profits = []

        for i in range(k):
            for project_i in range(len(cap_profit_heap)):
                cap, profit = cap_profit_heap[0]

                if cap <= w:
                    heapq.heappush(available_projects_profits, profit * -1)
                    heapq.heappop(cap_profit_heap)
                else:
                    break

            if len(available_projects_profits) == 0:
                return w

            w += heapq.heappop(available_projects_profits) * -1

        return w


if __name__ == '__main__':
    m = Solution().findMaximizedCapital(1, 2, [1,2,3], [1,1,2])
    print(m)
    # m = Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1])
    # print(m)
