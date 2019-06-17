class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if not nums:
            return 0
        tail = 0
        pre_value = None
        for head in range(len(nums)):
            if nums[head] != pre_value:
                nums[tail] = nums[head]
                tail += 1
                pre_value = nums[head]
                
        del nums[tail:]
                
        return tail
    
    
if __name__ == "__main__":
    nums = [1, 1, 2]
    s = Solution()
    print(s.removeDuplicates(nums))
    print(nums)