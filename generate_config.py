import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("common_settings")

# ADD SETTINGS TO SECTION
config_file.set("common_settings", "gtfs_history_data_root", "C:\\Users\AYAB\OneDrive - Drexel University\drexel\DSCI 591\detour project\data\GTFS-RT-historical-2022")

# SAVE CONFIG FILE
with open(r"GTFS-detour\configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("GTFS-detour\configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()
