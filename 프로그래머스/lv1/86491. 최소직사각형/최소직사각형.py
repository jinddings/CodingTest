def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b
    
def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0 
    
    
    for size in sizes :
        width, height = size[0], size[1]
        if width < height:
            width, height=  swap(width, height)
        max_width = max(max_width, width)
        max_height = max(height, max_height)
    
    answer = max_width * max_height
    return answer