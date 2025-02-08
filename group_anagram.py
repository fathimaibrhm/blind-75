
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        holder = defaultdict(list)

        for items in strs:
            freq = [0] * 26
            for c in items:
                freq[ord(c) - ord('a')] += 1

            holder[tuple(freq)].append(items)
        return list(holder.values())
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         holder = defaultdict(list)
#
#         for thingy in strs:
#             countedS = "".join(sorted(thingy))
#             holder[countedS].append(thingy)
#         return list(holder.values())

if __name__ == "__main__":
    solution = Solution()

    cases = [ ["eat","tea","tan","ate","nat","bat"], [""] , ["a"]]

    for item in cases:
        result = solution.groupAnagrams(item)
        print(result)





