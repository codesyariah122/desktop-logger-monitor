import os
import re

def extract_functions_and_classes(file_path):
    """
    Extracts functions and classes from a given Python file, adds the imports to each file,
    and saves them into separate files.
    """
    with open(file_path, 'r') as f:
        code = f.read()

    # Regular expressions to match Python functions, classes, and imports
    function_pattern = re.compile(r'^\s*def (\w+)\(.*\):', re.MULTILINE)
    class_pattern = re.compile(r'^\s*class (\w+)\(.*\):', re.MULTILINE)
    import_pattern = re.compile(r'^\s*(import .*|from .* import(?:.*\n\s*.*)*)', re.MULTILINE)

    # Find all function names
    functions = function_pattern.findall(code)
    # Find all class names
    classes = class_pattern.findall(code)
    # Find all imports
    imports = import_pattern.findall(code)

    # Make directories to save functions and classes
    output_dir = "modules"
    os.makedirs(output_dir, exist_ok=True)

    # Split and save functions to separate files with imports included
    for function in functions:
        function_code = extract_code_block(code, function, 'def ')
        with open(os.path.join(output_dir, f"{function}.py"), 'w') as f:
            # Write imports at the top of the file
            f.write("\n".join(imports) + "\n\n")
            f.write(f"# Function: {function}\n\n")
            f.write(function_code)
        print(f"Function {function} saved to {function}.py")

    # Split and save classes to separate files with imports included
    for cls in classes:
        class_code = extract_code_block(code, cls, 'class ')
        with open(os.path.join(output_dir, f"{cls}.py"), 'w') as f:
            # Write imports at the top of the file
            f.write("\n".join(imports) + "\n\n")
            f.write(f"# Class: {cls}\n\n")
            f.write(class_code)
        print(f"Class {cls} saved to {cls}.py")

def extract_code_block(code, name, type_):
    """
    Extracts the code block for a given function or class from the source code.
    """
    # Adjusting the pattern to capture everything within the function or class
    pattern = re.compile(rf'{type_}{name}\(.*\):.*?(?=^\s*(def |class |$))', re.DOTALL | re.MULTILINE)
    match = pattern.search(code)
    if match:
        return match.group(0)
    return ""

def main():
    file_path = 'activity-monitor.py'  # Path to the long Python file
    extract_functions_and_classes(file_path)

if __name__ == "__main__":
    main()
