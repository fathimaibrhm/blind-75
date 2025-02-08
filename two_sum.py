
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        holder = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in holder:
                return holder[compliment], i
            holder[nums[i]] = i

if __name__ == "__main__":
    solutionn = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target} → indices: {solutionn.twoSum(nums, target)}")

