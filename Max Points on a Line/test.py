def maxPoints(points):
    if len(points) < 3:
        return len(points)
    
    max_count = 0
    
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            count = 2  # At least 2 points on the line: points[i] and points[j]
            for k in range(j + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                
                # Check if the three points are collinear
                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    count += 1
            
            max_count = max(max_count, count)
    
    return max_count



points1 = [[1, 1], [2, 2], [3, 3]]
print(maxPoints(points1))  # Output: 3

points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(maxPoints(points2))  # Output: 4
