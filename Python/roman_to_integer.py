class Solution:
    
    roman_numbers = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
    
    def romanToInt(self, s: str) -> int:
        print(f'{s}')
        for i in range(len(s)):
            print(i)
        
        
def main() -> None:
    solution = Solution()
    print(solution.romanToInt("III"))
    
if __name__ == "__main__":
    main()
