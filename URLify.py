# Replace all spaces in a string with "%20"
# Time Complexity: O(n) - single pass through the string
# Space Complexity: O(n) - create a new string

def URLify(str):
    builder = ""
    startIdx = 0
    endIdx = 0
    for c in str:
        if c == " ":
            builder += str[startIdx : endIdx]
            builder += "%20"
            endIdx += 1
            startIdx = endIdx
        else:
            endIdx += 1
    builder += str[startIdx : ]
    return builder

def main():
    print(URLify("grit is fundamentally an expression of something you love"))

if __name__ == '__main__':
    main()