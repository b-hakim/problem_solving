class Solution1(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        window_start = 0
        max_sum = 0
        sums = {fruits[0]: 1}

        for i in range(1, len(fruits)):
            curr_sum = sum(sums.values())
            if max_sum < curr_sum:
                max_sum = curr_sum

            if len(sums.keys()) == 2:
                if fruits[i] in sums:
                    sums[fruits[i]] += 1
                else:
                    if fruits[window_start] == fruits[i-1]:
                        w = 0
                        for j in range(window_start, i):
                            if fruits[window_start] == fruits[i-1]:
                                w += 1
                            else:
                                break
                        sums[fruits[window_start]] -= w
                        window_start = j
                        sums[fruits[window_start]] -= 1
                    else:
                        sums.pop(fruits[window_start])

                    w = 0
                    for j in range(window_start, i):
                        if fruits[window_start] == fruits[j]:
                            w += 1
                        else:
                            break

                    sums[fruits[i]] = 1
                    window_start += w
            else:
                if fruits[i] in sums:
                    sums[fruits[i]] += 1
                else:
                    sums[fruits[i]] = 1

        curr_sum = sum(sums.values())

        if max_sum < curr_sum:
            max_sum = curr_sum

        return max_sum


class Solution_search(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        type1 = fruits[0]
        type2 = -1
        count_taken = 1
        max_count = 1

        if len(fruits) > 1:
            count_taken = 2
            max_count = 2
            if type1 != fruits[1]:
                type2 = fruits[1]

        starting_idx = 0

        for i in range(2, len(fruits)):
            if type2 == -1 and fruits[i] != type1:
                type2 = fruits[i]
                count_taken += 1
                continue

            if fruits[i] == type1 or fruits[i] == type2:
                count_taken += 1
            else:
                # update starting_idx --> loop on from [s, i] make sure type1 and mark last type1 pos
                # update type1
                # update type2
                if count_taken > max_count:
                    max_count = count_taken

                starting_idx += 1
                selected_type = type2 if type1 == fruits[i-1] else type1

                for j in range(starting_idx, i):
                    if fruits[j] == selected_type:
                        starting_idx = j+1

                new_count = i - starting_idx + 1


                count_taken = new_count
                type1 = type2 if type1 == selected_type else type1
                type2 = fruits[i]

        if count_taken > max_count:
            max_count = count_taken

        return max_count


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        type1 = fruits[0]
        type2 = -1
        count_taken = 1
        max_count = 1

        if len(fruits) > 1:
            count_taken = 2
            max_count = 2
            if type1 != fruits[1]:
                type2 = fruits[1]

        starting_idx = 0

        for i in range(2, len(fruits)):
            if type2 == -1 and fruits[i] != type1:
                type2 = fruits[i]
                count_taken += 1
                continue

            if fruits[i] == type1 or fruits[i] == type2:
                count_taken += 1
            else:
                # update starting_idx --> loop on from [s, i] make sure type1 and mark last type1 pos
                # update type1
                # update type2
                if count_taken > max_count:
                    max_count = count_taken

                starting_idx += 1
                selected_type = type2 if type1 == fruits[i-1] else type1

                for j in range(starting_idx, i):
                    if fruits[j] == selected_type:
                        starting_idx = j+1

                new_count = i - starting_idx + 1


                count_taken = new_count
                type1 = type2 if type1 == selected_type else type1
                type2 = fruits[i]

        if count_taken > max_count:
            max_count = count_taken

        return max_count


if __name__ == '__main__':
    print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
    print(Solution().totalFruit([1,0,1,4,1,4,1,2,3]))
    print(Solution().totalFruit([1,0,3,4,3]))
    print(Solution().totalFruit([1,2,1]))
    print(Solution().totalFruit([0,1,2,2]))
    print(Solution().totalFruit([1,2,3,2,2]))