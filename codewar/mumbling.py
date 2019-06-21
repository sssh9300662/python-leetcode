def accum(s):
    count = 0
    result = ""
    
    for v in s:
        count = count +1
        for k in range(count):
            if k == 0:
                result = result + v.upper()
            else:
                result = result + v.lower()
        result = result + "-"

    return result[:(len(result)-1)]


if __name__ == "__main__":
    print(accum("ZpglnRxqenU"))
