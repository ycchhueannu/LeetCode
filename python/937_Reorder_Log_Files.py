class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        log_letter = []
        log_digit = []
        for log in logs:
            log_split = log.split(' ')
            if log_split[1].isalpha():
                log_letter.append([log_split[0], ' '.join(log_split[1:])])
            else:
                log_digit.append(log)
        log_letter.sort(key=lambda x: (x[1], x[0]))
        log_letter = list(map(lambda x: ' '.join(x), log_letter))
        return log_letter + log_digit