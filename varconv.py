# Function to convert the values
def convert_to_camel_case(value):
    value = value.replace("$BASE_URL", "'$baseUrl'")
    value = value.replace("$VERSION", "'$version'")
    return value.lower()

# Prompt the user for input
print("Enter the environment variable values, one per line. Type 'done' when finished:")

# Read input from the console
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

# Process each line and print the result with the "final String" prefix, excluding empty strings
for line in lines:
    if line.strip(): # Check if the line is not empty
        converted_line = convert_to_camel_case(line)
        print(f"final String {converted_line}")
    else:
        print() # Print an empty line if the input was empty

