class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            ss = ''.join(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss] = [s]

        result = []
        for _, v in d.items():
            result.append(v)

        return result