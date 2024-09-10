class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap= defaultdict(list)
        for string in strs: hashMap[''.join(sorted(list(string)))].append(string)
        return hashMap.values()