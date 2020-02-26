class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        #brute force
            #solve for area of both triangles abcd and efgh and subtract the overlap
        
        #temp AC = c-a, DB = d-b; 
        R1 = Rect(A, B, C, D)
        R2 = Rect(E, F, G, H)
        
        overlap = Rect(max(A, E), max(B, F), min(C, G), min(D, H))
                       
        total = (R1.size + R2.size - overlap.size)
                    
        return total
        
class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        #calculate area = base * width
        
        if y2-y1<0 or x2-x1<0:       #check for invalid input size
            self.size = 0
        else:
            self.size = (x2-x1)*(y2-y1)
            
            
            
            #hindsight analysis, tests knowledge of structures. 
            #finding the problem is basic math and syntax, easy to mess up!
            
            #max = where two points meet positive x/y directions
            #min = where two points meet negative x/y directions