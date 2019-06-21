def longest_consec(strarr, k):
    if not strarr or k <= 0 or len(strarr) <= k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key=len)
        

if __name__ == "__main__":
    print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
