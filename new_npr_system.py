# List of offense codes mapped to their descriptions
offense_codes = {
    "S01": "Speeding",
    "S02": "Red Light Violation",
    "S03": "Reckless Driving",
    "S04": "Unlawful Parking",
    "S05": "Driving without Insurance"
}

# List of UK-style number plates with corresponding offense codes
input_number_plates_with_offenses = [
    ("AB12 XYZ", "S01"),
    ("CD34 WXY", "S02"),
    ("EF56 ZYX", "S03"),
    ("GH78 RST", "S02"),
    ("IJ90 QRS", "S04"),
    ("KL12 STU", "S05"),
    ("MN34 RST", "S01"),
    ("OP56 QRS", "S01"),
    ("QR78 STU", "S03"),
    ("ST90 RST", "S01"),
]

def npr_system(input_number_plates_with_offenses, query_number_plates, offense_codes):
    # make a list to store the results
    results = []
    
    # move through the list of query number plates
    for query in query_number_plates:
        # Initialize a list to store the offenses for the current query number plate
        offenses = []
        
        # move through the list of input number plates with offenses
        for plate, offense_code in input_number_plates_with_offenses:
            # If the query number plate matches the input number plate
            if plate == query:
                # add the corresponding offense description to the offenses list
                offenses.append(offense_codes[offense_code])
        
        # add the query number plate and its offenses to the results
        results.append((query, offenses))
    
    # Return the final results
    return results

# List of query number plates to check
query_number_plates = ["AB12 XYZ", "CD34 WXY", "KL12 STU", "NOP-000"]

# Call the NPR system function
result = npr_system(input_number_plates_with_offenses, query_number_plates, offense_codes)

# Format and print the result in an end-user-friendly way
for plate, offenses in result:
    print(f"Number Plate: {plate}") # Print the number plate
    if offenses:
        print("Offences Committed:")
        for offense in offenses:
            print(f"- {offense}") # print each offense committed
    else:
        print("No offences found.") # Print message if no offenses found
    print()
