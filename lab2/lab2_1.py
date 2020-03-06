import math
def vector_from_points(p1, p2):
    '''(list --> list)
        Function takes two points and subtracts the first point's indecies from the second point's
	to return a vector.

	Example: vector_from_points([0, 0], [1, 2]) returns [1,2]
    '''
    i = 0
    new_vector = []
    while i < len(p1):
        new_vector.append(p2[i] - p1[i])
        i += 1
    return new_vector

def vector_length(v):
    '''(list --> num)
	Function finds the magnitude of the vector by using the formula for euclidean distance.
	
	Example: vector_length([2, 1]) returns 2.23606797749979
    '''
    if v == []:
        return -1
    i = 0
    vector = 0
    while i < len(v):
        vector = math.hypot(vector, v[i])
        i += 1
    return vector

def angle_between(v, w):
    '''(list --> num)
	Function uses the rearranged dot product formula to solve for the angle between two vectors.

	Example: angle_between([-1], [2]) returns 180.0
    '''
    return math.degrees(math.acos(dot_product(v,w) / (vector_length(v) * vector_length(w))))

def dot_product(v,w):
    '''(list --> num)
	Function takes the dot product of two vectors by multiplying their directional scalars in R^n
	and then taking their sum. Program assumes both v and w are both in R^n.

	Example: dot_product([-1], [2]) returns -2
    '''
    i = 0
    mag_vector = 0
    while i < len(v):
        mag_vector += v[i]*w[i]
        i += 1
    return mag_vector

def unit_vector(v):
    '''(list --> list)
	Function takes vector coordinates and returns the vector coordinate if the vector length was
	equal to 1. Function returns an empty list if vector presented has no coordinates

	Example: unit_vector([2,1]) return [0.8944271909999159, 0.4472135954999579]
    '''
    unit_vector = []
    if v == []:
        return []
    for i in v:
        unit_vector.append(i/vector_length(v))
    return unit_vector

def cross_product(v,w):
    '''(list --> list)
	Takes the cross product of two vectors in R^3 by multiplying various indices. Returns empty
	list if vector is in more dimensions than R^3. Vectors in less than R^3 are computed with
	zero for empty values.

	Example: cross_product([1, 1, 1], [5.5, 5.5, 5.5]) returns [24, -6, 0]
    '''
    if (len(v) or len(w)) > 3:
        return []
    while len(v) < 3:
        v.append(0)
    while len(w) < 3:
        w.append(0)

    i = v[1]*w[2] - v[2]*w[1]
    j = v[2]*w[0] - v[0]*w[2]
    k = v[0]*w[1] - v[1]*w[0]

    return [i, j, k]

def scalar_projection(v,w):
    '''(list --> num)
	Takes the length of the projected vector of w onto v.

	Example: scalar_projection([0, 3], [1.5, 2]) returns 2.0
    '''
    return dot_product(v,w) / vector_length(v)
def vector_projection(v,w):
    '''(list --> list)
	Takes the dot product of the two vectors and divides it by the squared magnitude of the
	vector being projected on.
	
	Example: vector_projection([-2], [1.5]) returns [1.5]
    '''
    projection = dot_product(v,w) / vector_length(v)**2

    i = 0
    while i < len(v):
        v[i] *= projection
        i += 1
    return v

if __name__ == "__main__":
# test your vector operations here
    print(vector_from_points([0, 0], [1, 2]))
    print(vector_from_points([3, -1, 0], [10, 0, 1]))
    print(vector_length([2, 1]))
    print(vector_length([]))
    print(angle_between([-1], [2]))
    print(angle_between([0, 1, 0, 1], [1, 3, 4, 5]))
    print(dot_product([-1], [2]))
    print(dot_product([0, 1, 0, 1], [1, 3, 4, 5]))
    print(dot_product([0, 0], [0, 0]))
    print(unit_vector([2, 1]))
    print(unit_vector([]))
    print(cross_product([], [2]))
    print(cross_product([2, 8], [1, 4, 3]))
    print(cross_product([1, 1, 1], [5.5, 5.5, 5.5]))
    print(cross_product([1, 1, 1, 0], [1, 5.5]))
    print(scalar_projection([-2], [1.5]))
    print(scalar_projection([0, 3], [1.5, 2]))
    print(vector_projection([-2], [1.5]))
    print(vector_projection([0, 3], [1.5, 2]))
    
    # v1 = [0, -2, 3]
    # v2 = [1, 1, 1]
