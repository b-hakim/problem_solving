from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            n = len(row)
            for i in range(n // 2):
                # [[1,1,0]]
                # n = 3

                row[i], row[n - i - 1] = row[n - i - 1], row[i]

                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0

                if row[n - i - 1] == 0:
                    row[n - i - 1] = 1
                else:
                    row[n - i - 1] = 0

            if n % 2 == 1:
                row[n // 2] = 0 if row[n // 2] == 1 else 1

        return image