class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_cnt = {}
        for rN in ransomNote:
            if rN in ransom_cnt:
                ransom_cnt[rN] += 1
            else:
                ransom_cnt[rN] = 1
        for m in magazine:
            if not ransom_cnt:
                return True
            if m in ransom_cnt:
                ransom_cnt[m] -= 1
                if ransom_cnt[m] == 0:
                    del ransom_cnt[m]
        
        if not ransom_cnt:
            return True
        else:
            return False