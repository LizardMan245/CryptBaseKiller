import os
import time

def check_and_delete_file(file_name, directory, interval):
    # Full path to the file
    file_path = os.path.join(directory, file_name)

    while True:
        # Check if the file exists
        if os.path.exists(file_path):
            print(f"File {file_name} found. Deleting...")
            os.remove(file_path)  # Delete the file
            print(f"File {file_name} deleted.")
        #else:
            #print(f"File {file_name} not found.")

        # Wait for the specified interval before checking again
        time.sleep(interval)

if __name__ == "__main__":
    # Specify the file name, directory, and check interval (in seconds)
    file_name = "CryptBase.dll"
    directory = "D:\Origin games\Plants vs Zombies Garden Warfare 2"
    interval = 1  # Check every 10 seconds

    # Start checking and deleting if found
    check_and_delete_file(file_name, directory, interval)
