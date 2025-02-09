from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # using bucket sort
        freq = [[] for i in  range(len(nums) +1 )]
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        for num ,value in count.items():
            freq[value].append(num)
        res = []
        for j in range(len(freq) - 1 , 0 , -1 ):
            for num in freq[j]:
                res.append(num)
                if len(res) == k:
                    return res



    # using dictionary and sorting
    #     freq_map = defaultdict(int)
    #     for num in nums:
    #
    #         freq_map[num] += 1
    #     sorted_dict = sorted(freq_map.keys() ,key = lambda x :freq_map[x], reverse= True)
    #     return sorted_dict[:k]




     # return [num for num, _ in Counter(nums).most_common(k)](using counter and most_ccommon from collections module)

if __name__ == "__main__" :
    solution = Solution()

    nums = [1, 1, 1, 2, 2,3 ]
    k = 2
    print(f"the {k} most frequent element is {solution.topKFrequent(nums, k)}")








