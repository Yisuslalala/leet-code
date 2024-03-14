class Solution(object):
    def group_anagrams(self, strs: list[str]):

        anagrams = {}

        for anagram in strs:
            sorted_anagram = sorted(anagram)
            joined_anagram = "".join(sorted_anagram)

            if joined_anagram not in anagrams:
                anagrams[joined_anagram] = []

            anagrams[joined_anagram].append(anagram)

        print(anagrams)
        return list(sorted(anagrams.values()))


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # "aet", "aet", "ant", "aet", "ant", "abt"

    solution = Solution()

    print(f"Test 1: {solution.group_anagrams(strs)}")


if __name__ == "__main__":
    main()
