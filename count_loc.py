import os
import argparse

def count_lines(directory):
    total_lines = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(('.py', '.js', '.java', '.cpp')):  # add other extensions as needed
                try:
                    with open(os.path.join(dirpath, filename), 'r', encoding='utf-8', errors='ignore') as file:
                        total_lines += sum(1 for _ in file)
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
    return total_lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines of code in a directory")
    parser.add_argument("directory", help="Path to the directory")

    args = parser.parse_args()

    if os.path.isdir(args.directory):
        lines_of_code = count_lines(args.directory)
        print(f'Total lines of code: {lines_of_code}')
    else:
        print(f"{args.directory} is not a valid directory")
