def persistence(n):
    def manipulate(strings, level):
        value = 1
        for string in strings:
            value  = value  * int(string)
        if value == int(strings):
            return 0, level
        level = level +1
        return value, level
    
    level = 0
    
    while(n>0):
        n, level = manipulate(str(n), level)
            
    return level


if __name__ == "__main__":
    print(persistence(999))