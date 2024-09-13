# Complete Python file handling assignment with all tasks

# File handling with creation, reading, appending, and error handling

try:
    # File creation and writing
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("The number 42 is often considered special.\n")
        file.write("Python file handling is very useful!\n")
    print("File created and content written successfully.")
    
    # Reading the file
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nFile Content After Initial Writing:")
    print(content)
    
    # Appending to the file
    with open("my_file.txt", "a") as file:
        file.write("Appending first additional line.\n")
        file.write("Appending second additional line.\n")
        file.write("File handling is now complete!\n")
    print("\nText appended successfully.")
    
    # Reading the file after appending
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nFile Content After Appending:")
    print(content)
    
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You don't have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile operations complete.")
