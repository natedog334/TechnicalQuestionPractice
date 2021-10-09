# Decide if one string is a permutation of another
# Time Complexity: O(3n) = O(n) - single pass through each string, then one more thru map
# Space Complexity: O(2n) = O(n) - create a map that contains potentially every character in each string

def isPerm(s1, s2):
    if len(s1) != len(s2):
        return False

    s1Map = dict()
    for c in s1:
        if c not in s1Map:
            s1Map.update({c : 1})
        else:
            s1Map[c] += 1
    s2Map = dict()

    for c in s2:
        if c not in s2Map:
            s2Map.update({c : 1})
        else:
            s2Map[c] += 1

    for key in s1Map.keys():
        if (key not in s2Map) or (s1Map[key] != s2Map[key]):
            return False

    return True

def main():
    print(isPerm("f", ""))

if __name__ == '__main__':
    main()