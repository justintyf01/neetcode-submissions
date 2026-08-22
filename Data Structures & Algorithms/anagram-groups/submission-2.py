class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = {}
        d = defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))

            count = [0] * 26

            for c in s:
                count[ord('a') - ord(c)] += 1
            
            d[tuple(count)].append(s)

        return list(d.values())