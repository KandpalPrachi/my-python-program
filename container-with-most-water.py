class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        l,r = 0, len(height) - 1
        max_area = (r - l) * min(height[l], height[r])
        
        while l < r:
            
            
            
            if height[l] < height[r]:
                l += 1
                
            else:
                r -=1
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
    
            
                
        return max_area      
        