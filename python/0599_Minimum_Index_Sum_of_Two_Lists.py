class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {v: i for i, v in enumerate(list1)}
        d2 = {v: i for i, v in enumerate(list2)}
        min_sum = float("inf")
        ret = []
        if len(d1) < len(d2):
            for i in d1:
                if i in d2:
                    cur_sum = d1[i] + d2[i]
                    if cur_sum < min_sum:
                        min_sum = cur_sum
                        ret = [i]
                    elif cur_sum == min_sum:
                        ret.append(i)
        else:
            for i in d2:
                if i in d1:
                    cur_sum = d1[i] + d2[i]
                    if cur_sum < min_sum:
                        min_sum = cur_sum
                        ret = [i]
                    elif cur_sum == min_sum:
                        ret.append(i)
        return ret