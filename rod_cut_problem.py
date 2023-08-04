def willCutRod(cuts, minLength):
    # get the total length of the rod as zero
    total_length = 0

    # move through the cuts from right to left (reverse order)
    for cut in reversed(cuts):
        # add the current cut length to the total length
        total_length += cut

        # If the total length becomes equal to or greater than minLength, return True
        if total_length >= minLength:
            return True

    # If all cuts are considered and the total length is still less than minLength, return False
    return False

# Example usage
cuts = [3, 5, 2, 4]
minLength = 6
print(willCutRod(cuts, minLength))  # Output will be True
