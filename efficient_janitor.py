def getMinTrips(weight, n):
    weight.sort()  # Sort the weights in ascending order
    left = 0       # Pointer to the lightest weight
    right = n - 1  # Pointer to the heaviest weight
    trips = 0      # Counter for the number of trips required

    # Continue while there are unpaired weights
    while left <= right:
        # If the heaviest weight is more than 1.99 or the sum of the lightest and eaviest weights is more than 3
        if weight[right] > 1.99 or (weight[left] + weight[right] > 3):
            trips += 1  # Add one trip for the heaviest weight
            right -= 1  # Move to the next heaviest weight
        else:
            # Add one trip for the pair of lightest and heaviest weights
            trips += 1
            left += 1  # Move to the next lightest weight
            right -= 1 # Move to the next heaviest weight

        # Break the loop if all weights have been paired or considered
        if left > right:
            break

    return trips  # Return the total number of trips

# Read the number of weights
n = int(input())
# Read the weights and convert them to a list of floats
weight = list(map(float, input().strip().split()))
# Call the function to calculate the minimuum number of trips and print the result
trips = getMinTrips(weight, n)
print(trips)
