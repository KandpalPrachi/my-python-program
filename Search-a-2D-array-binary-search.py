class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        # now need to find the row and collumn in whic we have a target. for this we use two pointers
        top, bottom = 0, rows - 1
        #given that the matrix is sorted. for that top <= bottom is used
        while top <= bottom:
            # we know that in binary search--- mid= l+r//2... but here we have top and bottom
            row = (top + bottom)//2
            # for right most value we use -1
            if target > matrix[row][-1]:
                bottom = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
                
                
        
        if not (top <= bottom):
            return False
        
        # second portion of binary search - now we get row and we use pointer for searching target
        row = (top + bottom)//2
        l, r = 0, cols - 1
        
        while l<=r:
            m = (l+r)// 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
            #if we never find the target..we return false 
            
        return False
        
        
        
            
        