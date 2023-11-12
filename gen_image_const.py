import os

folder_path = "images/"  # Update this with the actual folder path
output_py_file = "img.py"  # The name of the output Python file

with open(output_py_file, "w") as f:
    f.write("# Auto-generated code\n\n")
    
    f.write("import configparser\n")
    f.write("config = configparser.ConfigParser()\n")
    f.write("config_file_path = 'bot.ini'\n")
    f.write("config.read(config_file_path)\n")
    f.write("settings = config['SETTINGS']\n")
    f.write("image_path = settings['image_path']\n\n")

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            variable_name = os.path.splitext(filename)[0]
            f.write(f"{variable_name} = image_path + '/{filename}'\n")

print("Code generation completed.")