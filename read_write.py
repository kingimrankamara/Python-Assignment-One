def read_and_write_file():
    # Ask the user for the input filename
    input_filename = input("Enter the input filename: ")
    
    try:
        # Open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()

        # Ask the user for the output filename
        output_filename = input("Enter the output filename: ")

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename} successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write to the file '{input_filename}' or '{output_filename}'.")

# Run the function
read_and_write_file()
