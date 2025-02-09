class Solution:

    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

if __name__ == "__main__":
    solution = Solution()

    strs = ["neet", "code", "love", "you"]
    result = solution.encode(strs)
    print (result)
    print(solution.decode(result))

