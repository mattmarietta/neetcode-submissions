class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Now that I have a unique key for that then I can append the words for that
            storage[tuple(count)].append(s)
        return list(storage.values())