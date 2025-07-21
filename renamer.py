import sys

# Get the file path and current file name
if len(sys.argv) == 3 :
    file_org = sys.argv[1]
    file_new = sys.argv[2]
    print(f"Original file: {file_org}\nNew file: {file_new}")
elif len(sys.argv) == 2 :
    if sys.argv[1] == '-h' :
        print("Usage: renamer.py [-h] filepath/original_filename.extension new_filename.extension")
    else:
        print("Missing a parameter. Type renamer.py -h for Help.")
else:
    print("Invalid options. Type renamer.py -h for Help.")

# If the file path is not provided, output a message and exit
# If the file path and file name are provided, check that the file exists
# If not, out put a message and exit


# Get the new file name


# Check the new file name for disallowed characters
# If it does, output a message and exit
sys.exit()


# Case-sensitive compare to ensure the new file name and extension <> the old file name and extension
# If it does, output a message and exit


# Print the old file name and new file name then prompt the user to confirm the change
# If confirmed, perform rename
# If not confirmed, output a message and exit