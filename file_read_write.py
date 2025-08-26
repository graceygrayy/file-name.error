# File Read & Write Challenge with Error Handling

def modify_content(content):
    """
    Function to modify the content.
    For example: convert text to uppercase.
    You can change this logic as needed.
    """
    return content.upper()

def main():
    # Ask the user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File has been modified and saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
