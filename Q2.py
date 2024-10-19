import re

def is_valid_number_plate(plate):
    # Define the regular expression pattern for the number plate format
    pattern = r"^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$"
    
    # Check if the plate matches the pattern
    if re.match(pattern, plate):
        return True
    else:
        return False

# Test the function
number_plate = input("Enter the number plate: ").strip()

if is_valid_number_plate(number_plate):
    print(f"{number_plate} is a valid Indian number plate.")
else:
    print(f"{number_plate} is not a valid Indian number plate.")
