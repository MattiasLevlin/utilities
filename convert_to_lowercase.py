# Example usage
# convert_to_lowercase('README.md')

def convert_to_lowercase(file_path):
    try:
        # Read the content of the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Convert the content to lowercase
        lower_content = content.lower()

        # Write the modified content back to the file with UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(lower_content)

        print(f"Successfully converted the content of {file_path} to lowercase.")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
