class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        cnt = 0
        diff_list = []
        record_alphabet = {}
        for a, b in zip(A, B):
            if a in record_alphabet:
                record_alphabet[a] += 1
            else:
                record_alphabet[a] = 1
                
            if a != b:
                diff_list.append([a, b])
                cnt += 1
                if cnt > 2:
                    return False
        # cnt should be 0, 1, 2
        if cnt == 2 and diff_list[0] == diff_list[1][::-1]:
            return True
        elif cnt == 0 and any(record_alphabet[i] > 1 for i in record_alphabet):
            return True
        else:
            return False