class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) in [0, 1]:
            return 0
        
        left, right = 0, len(height)-1
        
        rect_area = lambda l, r: min(height[l], height[r]) * (r - l)
        cur_max = rect_area(left, right)
        
        while left < right - 1:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            new_rect = rect_area(left, right)
            if new_rect > cur_max:
                cur_max = new_rect
        
        return cur_max