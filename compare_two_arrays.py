def are_arrays_equal(array1, array2):
    return array1 == array2

# Example usage
array1 = [3, 5, 2, 4]
array2 = [3, 5, 2, 4]
array3 = [4, 2, 5, 3]

print(are_arrays_equal(array1, array2))  # Output will be True
print(are_arrays_equal(array1, array3))  # Output will be False
