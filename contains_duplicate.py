#brute force approach
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#
#         return False

#sorting before iterating
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         nums.sort()
#
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False

# this is using set
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        collect = set()

        for num in nums:
            if num in collect:
                return True
            collect.add(num)
        return False

if __name__ == "__main__":
    solution = Solution()

    nums = [1,4,3,1]
    print(solution.containsDuplicate(nums))

    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums))
