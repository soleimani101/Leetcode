
from math import dist

import matplotlib.pyplot as plt

# points =[[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]]



# points = [[1,1],[2,2],[3,3]]
points =[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

class Solution(object):
    def maxPoints(self , points):
        counter = 0
        maxval = 0 
        if(len(points) == 1):
            return 1
        for index,point  in enumerate(points):
            shiblist = []
            for index_prime , point_prime in enumerate(points):
                
                a1 = point[0]
                a2 = point[1]
                b1 = point_prime[0]
                b2 = point_prime[1]
                if(a1 == b1 and a2 == b2):
                    shiblist.append(500)
                elif(b1-a1 != 0):
                    shib = (b2-a2)/(b1-a1)
                    shiblist.append(float(shib))
                else: 
                    shiblist.append(1000)
            print(shiblist)
            for shib in shiblist:
                counter = 0
                # print("reset-------------------------------")
                for shib2 in shiblist:
                        
                    if( float(shib) == float(shib2)  ): 
                        counter+=1
                        if counter > maxval:
                            maxval = counter
                    # print(counter , (shib) ,(shib2),((shib) ==(shib2) and shib != 500))
            print(shiblist)
            
            
        return maxval +1            





def plot_points(points, targetpoints):
    x_target= [point[0] for point in targetpoints]
    y_target= [point[1] for point in targetpoints]
    
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    

    plt.scatter(x, y,edgecolors="blue")
    plt.scatter(x_target, y_target,edgecolors="red")
    plt.plot(x_target,y_target, '-o')  # Connect the points with lines and display dots at each point

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points')
    plt.grid(True)
    plt.show()

# Example usage


max = Solution().maxPoints(points)
# plot_points(points, targetpoints)


print("final ******")
print(max)