class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(numRows):     
            tri = [1] * (i + 1)                                                 
            if (i + 1) > 2:                                       
                for j in range(len(result[-1]) - 1):
                    new_tri = result[-1][j] + result[-1][j+1]         
                    tri[0] = 1                                  
                    tri[-1] = 1
                    tri[j+1] = new_tri
            result.append(tri)   
            
        return result