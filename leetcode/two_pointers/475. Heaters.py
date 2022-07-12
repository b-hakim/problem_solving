from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # loop on each house
        # get the closest heater
        # track the maximum distance so far

        houses.sort()
        heaters.sort()

        p1, p2 = 0, 0
        max_distance = -1

        # houses = [1,2,3, 4], heaters = [1, 4]
        #         p1, p2 = 3, 1
        #         max_distance = 1

        while p1 != len(houses):
            if houses[p1] <= heaters[p2]:
                d = heaters[p2] - houses[p1]
                if d > max_distance:
                    max_distance = d
            else:  # houses[p1] > heaters[p2]:
                min_d = 1000000

                while p2 != len(heaters) and houses[p1] > heaters[p2]:
                    min_d = houses[p1] - heaters[p2]
                    p2 += 1

                if p2 == len(heaters):
                    p2 -= 1
                else:
                    # compare heater at p2 (which is > location of houses[p1])
                    d = heaters[p2] - houses[p1]

                    if d >= min_d:
                        p2 -= 1
                    else:
                        min_d = d

                if min_d > max_distance:
                    max_distance = min_d

            p1 += 1

        return max_distance