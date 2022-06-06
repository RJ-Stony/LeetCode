class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        inf = float('inf')
        ans = -1
        
        for i in range(len(points)):
            a, b = points[i]
            if a == x or b == y:
                dis = abs(a-x) + abs(b-y)
                if dis < inf:
                    inf, ans = dis, i
                    
        return ans