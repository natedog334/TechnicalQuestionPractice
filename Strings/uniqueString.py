# Determine if a string has all unique characters
# Time Complexity: O(n) - single pass through the string
# Space Complexity: O(n) - create a set that contains potentially every character in the string

def isUnique(str):
    if len(str) == 0:
        return True
    seen = set()
    for c in str:
        if c in seen:
            return False
        seen.add(c)
    return True

def main():
    print(isUnique("were"))

if __name__ == '__main__':
    main()