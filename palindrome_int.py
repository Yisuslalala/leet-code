class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        half_x = 0
        while x > half_x:
            half_x = (half_x * 10) + (x % 10)
            print(f"operation value: {x % 10}")
            x = x // 10
            print(f"{x}, {half_x}")
        
        return x == half_x or x == half_x // 10

def main() -> None:
    solution = Solution()
    print(solution.isPalindrome(1234321))
    print(solution.isPalindrome(123321))
    

if __name__ == "__main__":
    main()
