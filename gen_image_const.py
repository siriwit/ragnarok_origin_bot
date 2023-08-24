import os

folder_path = "images/"  # Update this with the actual folder path
output_py_file = "img.py"  # The name of the output Python file

with open(output_py_file, "w") as f:
    f.write("# Auto-generated code\n\n")
    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            variable_name = os.path.splitext(filename)[0]
            f.write(f"{variable_name} = 'images/{filename}'\n")

print("Code generation completed.")