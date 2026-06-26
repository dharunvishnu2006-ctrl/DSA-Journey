def group_anagrams(words):
    anagram_map = {}

    for word in words:
        
        key = "".join(sorted(word))

        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)
    return list(anagram_map.values())
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))