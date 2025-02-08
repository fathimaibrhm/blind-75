class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        holder = {}

        for ch in s:
            holder[ch] = holder.get(ch, 0) + 1

        for ch in t:
            holder[ch] = holder.get(ch, 0) - 1

        for values in holder.values():
            if values != 0:
                return False
        return True
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#
#         freq = [0] * 26
#
#         for ch in s:
#             freq[ord(ch) - ord('a')] += 1
#
#         for ch in t:
#             freq[ord(ch) - ord('a')] -= 1
#
#         for count in freq:
#             if count != 0:
#                 return False
#         return True

if __name__ == "__main__":
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))


