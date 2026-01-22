import os
import shutil

def duplicate_log_file():
    # Original log file name
    original_file = './app.log'

    # Check if the file exists
    if not os.path.exists(original_file):
        print(f"Error: {original_file} not found.")
        return

    # Create 5 copies
    for i in range(1, 6):
        new_file = f"app_{i}.log"
        shutil.copy(original_file, new_file)
        print(f"Created {new_file}")

if __name__ == "__main__":
    duplicate_log_file()
