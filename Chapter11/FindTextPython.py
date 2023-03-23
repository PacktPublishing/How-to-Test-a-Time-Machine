import re
file_to_analyse= open("fileName.txt", "r")
found_string = re.findall("stringToFind",
file_to_analyse.read())