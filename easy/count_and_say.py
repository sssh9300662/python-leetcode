class Solution:
    def countAndSay(self, n: int) -> str:
        def say(num:int, strings:str)->str:
            if num == 0:
                return "1"
            count = 0
            result = ""
            current = None
            
            for string in strings: 
                if string != current:
                    if current:
                        if count == 0:
                            result += ("1" + str(current))
                        else:
                            result += (str(count) + str(current))
                        count = 1
                    else:
                        count += 1
                    current = string
                else:
                    count += 1 
            
            if count == 0 and current:
                result += ("1" + str(current))      
            else:
                result += (str(count) + str(current))
            return result
            
        val = "1"
        for _ in range(0,n):
            val = say(_, val)
        return val 
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(5))