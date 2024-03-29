# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original 
# letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]


def GroupAnagrams(strs: list) -> list: 
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
        
    return list(anagram_map.values())


def main() -> None:
    print(GroupAnagrams(strs_1))
    
    
if __name__ == "__main__":
    main()