#  convert the values and variable names to camelCase
def convert_to_camel_case(value):
    # Split the input into variable name and value
    parts = value.split('=', 1)
    if len(parts) != 2:
        return value # Return the input unchanged if it doesn't have a '='
    
    # Extract the variable name and value
    var_name, var_value = parts
    
    # Convert the variable name to camelCase
    var_name = var_name.replace("_", "").lower()
    
    # Replace $BASE_URL and $VERSION in the value
    var_value = var_value.replace("$BASE_URL", "$baseUrl")
    var_value = var_value.replace("$VERSION", "$version")
    
    # Return the formatted string
    return f"{var_name} = '{var_value}'"

# Prompt the user for input
print("Enter the environment variable values, one per line. Type 'done' when finished:")

# Read input from the console
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

# Process each line and print the result, excluding empty strings
for line in lines:
    if line.strip(): # Check if the line is not empty
        converted_line = convert_to_camel_case(line)
        print(converted_line)
    else:
        print() # Print an empty line if the input was empty

