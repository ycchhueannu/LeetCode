class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        space = maxWidth # remaining space for each line
        retList = [] # return list of lines (scentences)
        line = [] # store words, will be converted to scentence
        
        def convLine2Str(l):
            if len(l) == 1:
                return l[0] + ' ' * (maxWidth - len(l[0]))
            num_space = maxWidth - sum([len(w) for w in l]) # remaining space, i.e. maxWidth - total chars in line
            num_slot = len(l) - 1 # ["xxx", "yyy", "zzz"] 3-word has 2 slots
            slot = [num_space // num_slot] * num_slot # each slot has at least number of "# spaces // # slot" spaces
            num_space -= (num_space // num_slot) * num_slot
            if num_space != 0:
                for i in range(0, len(slot)):
                    slot[i] += 1
                    num_space -= 1
                    if num_space == 0:
                        break
            slot = [' ' * i for i in slot]
            # see https://stackoverflow.com/questions/7946798/interleaving-two-lists-in-python
            scentence = l + slot
            scentence[::2] = l
            scentence[1::2] = slot
            scentence = ''.join(scentence)
            return scentence
        

        for w in words:
            if space >= len(w):
                line.append(w)
                space -= (len(w) + 1) # one means at least one space
            else:
                s = convLine2Str(line) # convert line to string
                retList.append(s)
                space, line = maxWidth, []
                
                line.append(w)
                space -= (len(w) + 1) # one means at least one space
        
        # last line need to be processed, note that we do not want extra spaces insert between words
        s = ' '.join(line)
        s += ' ' * (maxWidth - len(s)) 
        retList.append(s)
                
        return retList