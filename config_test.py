import configparser

# Initialize the configparser
config = configparser.ConfigParser()

# Specify the path to your configuration file
config_file_path = 'bot.ini'

# Read the configuration file
config.read(config_file_path)

# Access specific sections and options from the configuration file
if 'SETTINGS' in config:
    section = config['SETTINGS']
    if 'OPTION_NAME' in section:
        option_value = section['OPTION_NAME']
        print(f"Value of OPTION_NAME: {option_value}")
    else:
        print("OPTION_NAME not found in the configuration file.")
else:
    print("SECTION_NAME not found in the configuration file.")
