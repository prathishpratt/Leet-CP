class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r,tot =0,n-1,0
        leftmax,rightmax = 0,0

        while(l<=r):
            if(height[l]<=height[r]):
                if height[l]>=leftmax:
                    leftmax = height[l]
                else:
                    tot = tot+ (leftmax-height[l])
                l +=1
            else:
                if height[r]>rightmax:
                    rightmax = height[r]
                else:
                    tot = tot + (rightmax-height[r])
                r -=1
        return tot