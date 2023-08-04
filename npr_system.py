def npr_system(input_number_plates, query_number_plates):
    # make a list to hold the results for each query number plate
    results = []
    
    # move through the query number plates
    for query in query_number_plates:
        # Use the count() method to find how many times the query number plate occurs in the input number plates
        count = input_number_plates.count(query)
        
        # add the count to the results list
        results.append(count)
    
    # Return the resulting list of counts
    return results

# Example usage
input_number_plates = ["XYZ-123", "ABC-456", "XYZ-123", "LMN-789"]
query_number_plates = ["XYZ-123", "LMN-789", "NOP-000"]
result = npr_system(input_number_plates, query_number_plates)
print(result)  # Output will be [2, 1, 0]
