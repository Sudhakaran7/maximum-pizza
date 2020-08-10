class Solution(object):
    def maxSizeSlices(self, slices):
        def helper(a, k):
            n = len(a)
            dp = [[0 for _ in range(k+1)] for _ in range(n)]
            dp[0][1] = a[0]
            for i in range(1, n):
                for j in range(1, k+1):
                    dp[i][j] = max(dp[i-1][j], dp[i-2][j-1]+a[i])
            return dp[n-1][k]
 
        return max(helper(slices[1:], len(slices)//3), helper(slices[:-1], len(slices)//3))
val=Solution()
n=int(input())
slices=list(map(int,input().split()))
print(val.maxSizeSlices(slices))
