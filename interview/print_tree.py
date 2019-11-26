class Solution:
    def print_tree(self, first: int, level: int) -> bool:
        max_elements = first + 2*(level-1)
        pre_element = "*"*first
        for i in range(level):
            if i != 0:
                pre_element = pre_element + "*"*2
            space = int((max_elements - len(pre_element))/2)
            print(" "*space + pre_element + " "*space)
            i = i + 1
            
            
if __name__ == "__main__":
    s = Solution()
    s.print_tree(1, 3)