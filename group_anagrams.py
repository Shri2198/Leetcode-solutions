class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for n in strs:
            sorted_wrd = ''.join(sorted(n))
            if sorted_wrd not in anagram:
                anagram[sorted_wrd] = []
            anagram[sorted_wrd].append(n)
        return list(anagram.values())