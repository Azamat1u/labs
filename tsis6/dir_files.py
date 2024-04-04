# ex1
import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
            all_directories_files.append(item)
        else:
            files.append(item)
            all_directories_files.append(item)

    print("Directories:", directories)
    print("Files:", files)
    print("All Directories and Files:", all_directories_files)

# Example usage
list_directories_files("/path/to/directory")






# ex2
import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print("Exists:", exists)
    print("Readable:", readable)
    print("Writable:", writable)
    print("Executable:", executable)

# Example usage
check_access("/path/to/file_or_directory")






# ex3
import os

def analyze_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

# Example usage
analyze_path("/path/to/file_or_directory")



# ex4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Example usage
print("Number of lines:", count_lines("example.txt"))




# ex5
def write_list_to_file(file_path, input_list):
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')

# Example usage
my_list = ['apple', 'banana', 'orange']
write_list_to_file("output.txt", my_list)




# ex5
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(letter + ".txt", 'w') as file:
            pass  # Do nothing, just create the file

# Example usage
generate_text_files()




# ex6
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)

# Example usage
copy_file("source.txt", "destination.txt")



# ex7
import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("File does not exist or access denied.")

# Example usage
delete_file("/path/to/file")