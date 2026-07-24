class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            key = tuple(sorted(s))
            store.setdefault(key, []).append(s)
        return list(store.values())
        