class Solution:

    # https://leetcode.com/problems/product-of-array-except-self/

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = []
        prefix_product = 1
        postfix_product = 1

        for i in range(len(nums)):

            if i == 0:
                answer.append(1)
                prefix_product = nums[i]
            else:
                answer.append(prefix_product)
                prefix_product *= nums[i]

        for j in range(len(nums) - 1, -1, -1):

            if j == len(nums) - 1:
                answer[j] *= 1
                postfix_product *= nums[j]
            else:
                answer[j] *= postfix_product
                postfix_product *= nums[j]

        return answer

    # Time Complexity: O(n) , Space Complexity: O(n) if we include output space for output otherwise O(1)
