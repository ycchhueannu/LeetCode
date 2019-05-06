class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dict_dom = {}
        for email in emails:
            local_name, domain_name = email.split('@')
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]
            local_name = ''.join(local_name.split('.'))
            
            if domain_name not in dict_dom:
                dict_dom[domain_name] = set({local_name})
            else:
                dict_dom[domain_name].add(local_name)
        cnt = 0
        for dom in dict_dom.keys():
            cnt += len(dict_dom[dom])
        return cnt