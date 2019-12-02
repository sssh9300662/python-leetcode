
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def max_target(s):
    target = ''
    for c in s:
        if c not in target:
            target = target + c
    size = len(target)
    return size

def shortestSubstring(s):
    unique = max_target(s)
    result = len(s)
    for i in range(len(s)):
        for j in range(len(s)):
            sub = s[i:j+1]
            size = len(sub)
            target = max_target(sub)
            if target == unique and size < result:
                result = size

    return result


if __name__ == '__main__':
    
    result = shortestSubstring('aabcce')
    print(result)
