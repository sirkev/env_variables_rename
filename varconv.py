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

# Process each line and print the result with the "final String" prefix
for line in lines:
    converted_line = convert_to_camel_case(line)
    print(f"final String {converted_line}")

