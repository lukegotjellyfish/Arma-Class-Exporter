import csv
import os
from pathlib import Path


def append_to_csv(text, directory, filename):
    """
    _z = ["neko.append_to_csv",["csv,contents,ok", "C:/here/", "file.csv"]] call py3_fnc_callExtension;
    """
    check_path_exists(directory,1)
    try:
        with open(os.path.join(directory, filename), 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(text)
    except Exception:
        # If function has raised an exception, return False to indicate failure
        return False
    # If function has completed, return True to indicate success
    return True

def check_path_exists(directory,filename="",make_dir=0):
    """
    _z = ["neko.check_path_exists",["C:/here/"]] call py3_fnc_callExtension;
    _z = ["neko.check_path_exists",["C:/here/file.txt"]] call py3_fnc_callExtension;
    _z = ["neko.check_path_exists",["C:/here/newDir_ifNotExist",1]] call py3_fnc_callExtension;
    """
    try:
        # Check if the directory already exists
        if not os.path.exists(os.path.join(directory, filename)):
            if filename != "" or make_dir == 0:
                # A filename has been supplied/make_dir==0 so we are checking if a file exists, return false as it does not
                return False
            # Create the directory
            if make_dir == 1:
                os.makedirs(directory)
    except Exception:
        # If function has raised an exception, return False to indicate failure
        return False
    # If function has completed, return True to indicate success
    return True

def write_to_file(text, directory, filename):
    """
    _z = ["neko.write_to_file",["writing to file", "C:/here/", "file.txt"]] call py3_fnc_callExtension;
    """
    check_path_exists(directory,1)
    try:
        with open(os.path.join(directory, filename), 'w') as file:
            file.write(text)
    except Exception:
        # If function has raised an exception, return False to indicate failure
        return False
    # If function has completed, return True to indicate success
    return True

def append_to_file(text, directory, filename):
    """
    _z = ["neko.append_to_file",["writing to file", "C:/here/", "file.txt"]] call py3_fnc_callExtension;
    """
    check_path_exists(directory,1)
    try:
        with open(os.path.join(directory, filename), 'a') as file:
            file.write(text)
    except Exception:
        # If function has raised an exception, return False to indicate failure
        return False
    # If function has completed, return True to indicate success
    return True