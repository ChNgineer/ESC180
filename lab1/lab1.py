# ESC180 Lab 1
# Connected Cows
# DO NOT modify any function or argument names

import math

def find_euclidean_distance(x1, y1, x2, y2):
    """
    The distance between two points on a 2-D plane can be found using the pythagorean theorem,
    by breaking down the distance into x and y components, orthogonal to each other. This function
    takes the difference between the x and y coordinates and plugs them into the pythagorean theorem
    to gauge distance in a straight line between two points.
    """
    x_vector = x2 - x1
    y_vector = y2 - y1

    hypotenuse = math.hypot(x_vector, y_vector)
    
    return(round(hypotenuse,2))

def is_cow_within_bounds(cow_position, boundary_points):
    """
    The cow's position relative to the boundary points can be guaged in 2-D by breaking it down into
    x and y components as domain and range. The cow's position in a single dimension can be viewed as
    a point, and the boundaries act as the maximum and minimum limit for the possible values of the cow's
    position on an imaginary numberline. Thus, if the cow is within the limit, return 1, otherwise
    return 0.
    """
    i = 0
    x = cow_position [0]
    y = cow_position [1]
    list_of_x_bounds = []
    list_of_y_bounds = []

    while(i <= 3):
        list_of_x_bounds.append(boundary_points[i][0])
        list_of_y_bounds.append(boundary_points[i][1])
        i = i + 1
    
    if(x < max(list_of_x_bounds) and x > min(list_of_x_bounds) and y < max(list_of_y_bounds) and y > min(list_of_y_bounds)):
        return(1)
    else:
        return(0)

def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    The distance between the cow's position and a boundary point can be taken as a distance in 2-D
    identical to the function find_euclidean_distance(x1, y1, x2, y2). Set the cow's position as x1
    and y1, and the boundary point as x2 and y2 and see docstring for
    find_euclidean_distance(x1, y1, x2, y2).
    """
    return(find_euclidean_distance(cow_position[0], cow_position[1], boundary_point[0], boundary_point[1]))

def find_time_to_escape(cow_speed, cow_distance):
    """
    In inertial frames of reference (no acceleration), time can be calculated as distance divided
    by time. Thus the time can be found by dividing the cow's distance and its speed.
    """
    time = cow_distance / cow_speed

    return(round(time,2))
    
def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    """
    This function is partitioned into 4 sections which can be determined with the function
    is_cow_within_bounds(cow_position, boundary_point) at two points in time.

    If both positions return 1, then the time to escape via the nearest boundary is taken. This is
    done by calling the find_time_to_escape(cow_speed, cow_distance) function with the velocity
    argument taken from find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0],
    cow_position2[1]) / delta_t and a distance argument of the minimum distances between the cow's
    2nd x position to the boundary's x positions, and the cow's 2nd y position to the boundary's y
    positions.

    If both positions return 0, then the time to return to boundary_points[0] is taken from the 
    cow's 2nd position. This can be done by calling the find_time_to_escape(cow_speed, cow_distance)
    function with the velocity and boundary_points[0] as the arguments.

    If the cow returns to the boundary, then the function will return -1.

    If the cow leaves the boundary, then the function will return 0.
    """
    velocity = find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1]) / delta_t
    
    if(is_cow_within_bounds(cow_position1, boundary_points) == 1 and is_cow_within_bounds(cow_position2, boundary_points) == 1):

        i = 0
        list_of_distances = []

        while(i <= 3):
            list_of_distances.append(abs(cow_position2[0] - boundary_points[i][0]))
            list_of_distances.append(abs(cow_position2[1] - boundary_points[i][1]))
            i = i + 1
        
        return(find_time_to_escape(velocity, min(list_of_distances)))
        
    elif(is_cow_within_bounds(cow_position1, boundary_points) == 0 and is_cow_within_bounds(cow_position2, boundary_points) == 0):

        return(find_time_to_escape(velocity, find_cow_distance_to_boundary(cow_position2, boundary_points[0])))

    elif(is_cow_within_bounds(cow_position1, boundary_points) == 0 and is_cow_within_bounds(cow_position2, boundary_points) == 1):
        return(-1)
    else:
        return(0)
            
if __name__ == '__main__':
    # Test your code by running your functions here, and printing the
    # results to the terminal.
    # This code will not be marked
    print('Testing functions...')
    # test_distance = find_euclidian_distance(3.0, 3.0, 2.0, 5.0)
    # print(test_distance)
    # test_distance should be 2.24
