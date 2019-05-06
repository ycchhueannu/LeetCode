class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        import re
        d = {}
        for path in paths:
            directory, *files = path.split(' ')
            for file in files:
                name, content, _ = re.split("[()]", file)
                if content not in d:
                    d[content] = [directory+'/'+name]
                else:
                    d[content].append(directory+'/'+name)
        return [value for key, value in d.items() if len(value) >= 2]