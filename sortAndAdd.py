import os

# Function to process a text file
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                # Try to convert the line to a float (ignore non-numeric lines)
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    pass

            if numbers:
                # Sort the numbers
                numbers.sort()

                # Create a new filename for the processed data
                processed_filename = "processed_" + filename

                # Write sorted numbers and their sum to the new file
                with open(processed_filename, 'w') as processed_file:
                    processed_file.write("Sorted Numbers:\n")
                    for number in numbers:
                        processed_file.write(str(number) + '\n')
                    processed_file.write("Sum of Numbers:\n")
                    processed_file.write(str(sum(numbers)))

                print(f"Processed: {filename} => {processed_filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Get a list of all files in the current directory
current_directory = os.getcwd()
files = os.listdir(current_directory)

# Process each file in the directory
for file in files:
    if file.endswith(".txt"):
        process_file(file)