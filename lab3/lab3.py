import utilities

def rotate_90_degrees(image_array, direction):
    output_array = []
    new_row = []
    if direction == 1:
        #Rotate Clockwise
        j = 0
        i = len(image_array[0]) -1
        while j < len(image_array[0]):
            while i > -1:
                new_row.append(image_array[i][j])
                i -= 1
            i = len(image_array[i]) -1
            output_array.append(new_row)
            new_row = []
            j += 1
    elif direction == -1:
        #Rotate Anti Clockwise
        i = 0
        j = len(image_array[i]) -1
        while j > -1:
            while i < len(image_array):
                new_row.append(image_array[i][j])
                i += 1
            i = 0
            output_array.append(new_row)
            new_row = []
            j -= 1
                 
    return output_array        

def flip_image(image_array, axis = 0):
    output_array = []
    new_row = []
    
    if axis == 0:
        #flip along y
        i = 0
        j = len(image_array[i]) -1
        while i < len(image_array):
            while j > -1:
                new_row.append(image_array[i][j])
                j -= 1
            j = len(image_array[i]) -1
            output_array.append(new_row)
            new_row = []
            i += 1
            
    elif axis == 1:
        #flip along x
        i = len(image_array) -1
        j = 0
        while i > -1:
            while j < len(image_array[i]):
                new_row.append(image_array[i][j])
                j += 1
            j = 0
            output_array.append(new_row)
            new_row = []
            i -= 1
            
    elif axis == -1:
        #flip along y = x
        new_array = rotate_90_degrees(image_array,1)
        i = len(new_array) -1
        j = 0
        while i > -1:
            while j < len(new_array[i]):
                new_row.append(new_array[i][j])
                j += 1
            j = 0
            output_array.append(new_row)
            new_row = []
            i -= 1
            
    return output_array

def invert_grayscale(image_array):
    i = 0
    j = 0
    output_array = []
    new_row = []

    while i < len(image_array):
        while j < len(image_array[i]):
            new_row.append(abs(255 - image_array[i][j]))
            j += 1
        output_array.append(new_row)
        new_row = []
        i += 1
        j = 0
        
    return output_array

    
def crop(image_array, direction, n_pixels):
    i = 0
    j = 0
    new_row = []
    output_array = []
    
    if direction == 'up':
        while n_pixels < len(image_array):
            output_array.append(image_array[n_pixels])
            n_pixels +=1
            
    elif direction == 'down':
        while i <= n_pixels:
            output_array.append(image_array[i])
            i +=1
            
    elif direction == 'right':
        new_array = rotate_90_degrees(image_array,1)
        while i <= n_pixels:
            output_array.append(new_array[i])
            i +=1        
        return rotate_90_degrees(output_array, -1)
    
    elif direction == 'left':
        new_array = rotate_90_degrees(image_array,1)
        while n_pixels < len(new_array):
            output_array.append(new_array[n_pixels])
            n_pixels +=1        
        return rotate_90_degrees(output_array, -1)
    
    return output_array

def rgb_to_grayscale(rgb_image_array):
    i = 0
    j = 0
    output_array = []
    new_row = []
    while i < len(rgb_image_array):
        while j < len(rgb_image_array[i]):
            new_row.append(round(rgb_image_array[i][j][0]*0.2989 + rgb_image_array[i][j][1]*0.5870 + rgb_image_array[i][j][2]*0.1140))
            j += 1
        output_array.append(new_row)
        new_row = []
        i += 1
        j = 0
        
    return output_array

def invert_rgb(image_array):
    i = 0
    j = 0
    k = 0
    output_array = []
    new_row = []
    new_set = []
    while i < len(image_array):
        while j < len(image_array[i]):
            while k < len(image_array[i][j]):
                new_set.append(255 - image_array[i][j][k])
                k += 1
            new_row.append(new_set)
            new_set = []
            j += 1
            k = 0
        output_array.append(new_row)
        new_row = []
        i += 1
        j = 0

    return output_array
'''    
def gaussian_blur(image_array, sigma=0.84089):

	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

	return output_array

def image_to_drawing(image_array):
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

	return output_array
'''
if (__name__ == "__main__"):
    file = 'robot.png'
    utilities.write_image(rotate_90_degrees(utilities.image_to_list(file),1), 'clockwise.png')
