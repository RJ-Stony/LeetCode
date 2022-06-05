class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sym_dict = {')':'(', '}':'{', ']':'['}
        
        for sym in s:
            if sym in sym_dict.values():
                stack.append(sym)
            elif sym in sym_dict.keys():
                if stack == [] or sym_dict[sym] != stack.pop():
                    return False
            else:
                return False
            
        return stack == []