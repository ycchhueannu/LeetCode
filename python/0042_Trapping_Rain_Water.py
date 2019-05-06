class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) - 2 <= 0:
            return 0

        left= []
        IDX, HGHT, BTM= 0, 1, 2
        END = -1
        drop = 0 # record number of droplets
        for idx, h in enumerate(height):
            #print("idx:", idx, "h:", h)
            
            if left == []:
                if h == 0:
                    #print("=================")
                    continue
                left.append([idx, h, h]) # index, height (top), y coordinate's start index (bottom)
                
            else: # left is not empty list
                
                if h == 0:
                    left[END][BTM] = 0
                    #print("left:", left)
                    #print("=================")
                    continue
                
                if h < left[END][HGHT]: # end of left, note that h > 0
                    if h < left[END][HGHT]:
                        length = idx - left[END][IDX] - 1
                        if length > 0:
                            drop += (h - left[END][BTM]) * length
                        left[END][BTM] = h
                    left.append([idx, h, h])
                else: # h >= left[END][HGHT]:
                    for _ in iter(int, 1): # infinite loop
                        length = idx - left[END][IDX] - 1
                        if length > 0:
                            drop += (left[END][HGHT]-left[END][BTM]) * length
                        
                        del left[END] # slow?
                        if left == []:
                            break
                            
                        if h < left[END][HGHT]:
                            length = idx - left[END][IDX] - 1
                            if length > 0:
                                drop += (h - left[END][BTM]) * length
                            left[END][BTM] = h
                            break
                    left.append([idx, h, h])
            
            #print("left:", left)
            #print("drop:", drop)
            #print("=================")
        return drop