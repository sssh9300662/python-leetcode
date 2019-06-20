def persistence(n):
    print("***********")
    vals = str(n)
    value = 1
    level = 0
    
    for val in vals:
        value  = value  * int(val)
     
    if value == int(vals):
        print("!!!!")
        return 0
    else:
        while(level>0):
            print(value)
            count = persistence(value)
            print("################")
            #print(count)
            
    return level


if __name__ == "__main__":
    print(persistence(999))