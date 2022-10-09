
import configparser

# Method to read config file settings
def read_config(Config_File):
    config = configparser.ConfigParser()
    config.read(Config_File)
    return config