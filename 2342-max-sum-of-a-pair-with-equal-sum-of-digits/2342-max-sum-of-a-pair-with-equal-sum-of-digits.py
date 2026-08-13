class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        largest = {}
        ans = -1

        for num in nums:
            digit_sum = sum(int(d) for d in str(num))

            if digit_sum in largest:
                ans = max(ans, num + largest[digit_sum])

            largest[digit_sum] = max(largest.get(digit_sum, 0), num)

        return ans
            