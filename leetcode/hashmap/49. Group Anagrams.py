class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        for word in strs:
            cnt = [0] * 26

            for letter in word:
                cnt[ord(letter) - ord('a')] += 1

            ret[tuple(cnt)].append(word)

        return ret.values()

# from typing import List
#
#
# def same_dict(m1, m2):
#     for k in m1:
#         if k not in m2 or m2[k] != m1[k]:
#             return False
#
#     for k in m2:
#         if k not in m1 or m1[k] != m2[k]:
#             return False
#
#     return True
#
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ret = []
#         cnt = []  # [{}, {}, {}]
#
#         for word in strs:
#             m = {}
#             for letter in word:
#                 if letter in m:
#                     m[letter] += 1
#                 else:
#                     m[letter] = 1
#
#             found = False
#
#             for i, dict in enumerate(cnt):
#                 if same_dict(m, cnt[i]):
#                     ret[i].append(word)
#                     found = True
#
#             if not found:
#                 ret.append([word])
#                 cnt.append(m)
#
#         return ret
#
# if __name__ == '__main__':
#     ret = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
#     print (ret)