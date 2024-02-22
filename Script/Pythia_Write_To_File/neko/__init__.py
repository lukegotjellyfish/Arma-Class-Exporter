import os
import logging


def write_to_file(text, directory, filename):
    """
    _z = ["neko.write_to_file",["writing to file", "C:/here/", "file.txt"]] call py3_fnc_callExtension;
    """

    try:
        # Check if the directory already exists
        if not os.path.exists(directory):
            # Create the directory
            os.makedirs(directory)
    except Exception:
        return

    try:
        with open(os.path.join(directory, filename), 'w') as file:
            file.write(text)
    except Exception:
        return
