def diagonal_difference(arr):
# Determine the size of the matrix    
n = int(len(arr) ** 0.5)  
    # Convert array into matrix
    matrix = [arr[i * n:(i + 1) * n] for i in range(n)]  

    primary_diagonal_sum = sum(matrix[i][i] for i in range(n))
    secondary_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))

    return abs(primary_diagonal_sum - secondary_diagonal_sum)

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(diagonal_difference(ar))  # Output will be 0
