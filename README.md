# CodeLineCounter

A simple Python tool to calculate the total lines of code (LOC) in a project directory, supporting various file types. It helps developers quickly assess the size and structure of their codebase by counting the number of lines in key source files.

## Features

- Supports multiple programming languages, including Python, JavaScript, Java, and C++
- Easily extensible to include additional file types
- Handles large directories and multiple files
- Skips non-code files and reports any errors during the file reading process

## How It Works

This tool walks through the specified directory and counts the lines in files that match specific extensions (`.py`, `.js`, `.java`, `.cpp`). The total number of lines is then printed out as the final output.

## Supported File Types

- Python (`.py`)
- JavaScript (`.js`)
- Java (`.java`)
- C++ (`.cpp`)

You can add more file extensions by modifying the following line in the script:

```python
if filename.endswith(('.py', '.js', '.java', '.cpp')):
```
