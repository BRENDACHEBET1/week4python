def modify_content(content):
    """
    Modify the content of the file. 
    This function can be customized to change the content as needed.
    """
    # Example modification: convert all text to uppercase
    return content.upper()

def read_and_write_file():
    # Get the filename from the user
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to write to: ")

    try:
        # Try opening and reading the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Successfully written modified content to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    
# Run the function
read_and_write_file()
