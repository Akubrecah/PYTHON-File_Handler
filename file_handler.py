import os

def read_file(filename):
    """
    Read content from a file with proper exception handling.
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        str: The content of the file if successful, None otherwise
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred while reading '{filename}': {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading '{filename}': {e}")
    return None

def write_file(filename, content):
    """
    Write content to a file with proper exception handling.
    
    Args:
        filename (str): The name of the file to write to
        content (str): The content to write to the file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to '{filename}'.")
        return True
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred while writing to '{filename}': {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while writing to '{filename}': {e}")
    return False

def modify_content(content):
    """
    Modify the content of the file by performing some transformations.
    
    Args:
        content (str): The original content
        
    Returns:
        str: The modified content
    """
    if content is None:
        return None
    
    # Example modifications:
    # 1. Convert to uppercase
    # 2. Add line numbers
    # 3. Remove extra whitespace
    
    # Remove extra whitespace and split into lines
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    # Add line numbers and convert to uppercase
    modified_lines = []
    for i, line in enumerate(lines, 1):
        modified_line = f"{i}. {line.upper()}"
        modified_lines.append(modified_line)
    
    # Join back with newlines
    return '\n'.join(modified_lines)

def main():
    """
    Main function to run the file handling program.
    """
    print("=" * 50)
    print("FILE HANDLING AND EXCEPTION HANDLING PROGRAM")
    print("=" * 50)
    
    # Get input filename from user
    input_filename = input("Please enter the name of the file to read: ")
    
    # Read the file
    content = read_file(input_filename)
    
    # If reading was successful, process and write to new file
    if content is not None:
        print(f"Successfully read '{input_filename}'.")
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Create output filename
        name, ext = os.path.splitext(input_filename)
        output_filename = f"{name}_modified{ext}"
        
        # Write the modified content to a new file
        success = write_file(output_filename, modified_content)
        
        if success:
            print("\nOperation completed successfully!")
            print(f"Original file: {input_filename}")
            print(f"Modified file: {output_filename}")
            
            # Optional: Display the content of both files
            display = input("\nWould you like to see the content of both files? (y/n): ").lower()
            if display == 'y':
                print(f"\nOriginal content of '{input_filename}':")
                print("-" * 40)
                print(content)
                
                print(f"\nModified content of '{output_filename}':")
                print("-" * 40)
                print(modified_content)
    else:
        print("Failed to read the file. Please check the filename and try again.")

if __name__ == "__main__":
    main()