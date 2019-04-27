class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x_c = x_center
        self.y_c = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        from numpy import random as rand
        inCircle = lambda x, y: (x-self.x_c)**2 + (y-self.y_c)**2 <= self.r**2
    
        while True:
            x_rand = rand.uniform(self.x_c-self.r, self.x_c+self.r)
            y_rand = rand.uniform(self.y_c-self.r, self.y_c+self.r)
            if inCircle(x_rand, y_rand):
                return [x_rand, y_rand]
                

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()