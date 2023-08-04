def left_rotate(array, d):
    # what is the actual number of rotations needed, considering the length of the array
    rotations = d % len(array)
    
    # Create a new rotated array
    rotated_array = [0] * len(array)

    # move through the original array
    for i in range(len(array)):
        # Calculate the new index for the element after performing the left rotation
        # if the new index becomes negative, it wraps around to the end of the array
        new_index = (i - rotations) % len(array)

        # Place the element in its new position in the rotated array
        rotated_array[new_index] = array[i]

    # Return the resulting rotated array
    return rotated_array

# Example usage
array = [1, 2, 3, 4, 5]
d = 2
result = left_rotate(array, d)
print(result)  # Output will be [3, 4, 5, 1, 2]
