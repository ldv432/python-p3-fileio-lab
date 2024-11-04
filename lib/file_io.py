def write_file(file_name, file_content):
     # Add .txt extension to the file name
    file_name = f"{file_name}.txt"
    # Open file in write mode and write content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
     # Add .txt extension to the file name
    file_name = f"{file_name}.txt"
    # Open file in append mode and add content
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Add .txt extension to the file name
    file_name = f"{file_name}.txt"
    # Open file in read mode and return its content
    with open(file_name, 'r') as file:
        return file.read()