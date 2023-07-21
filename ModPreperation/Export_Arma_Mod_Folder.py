import os
import glob
import re
import sys
import subprocess
from datetime import datetime

"""
Requirements:
 Requres the following on PATH:
  pboman3 (pboc)     https://github.com/winseros/pboman3
  CfgConvert         https://community.bistudio.com/wiki/CfgConvert
  EBODecunter        https://www.unknowncheats.me/forum/arma-3-a/354908-ebodecunter-1-1-decrypts-dlc-ebos.html
  
 Will later require
  DeP3D              https://community.bistudio.com/wiki/DeP3d
  Pal2PacE           https://community.bistudio.com/wiki/TexView_2
  Disabling the OptiPNG function will save a lot of time, disabling dep3d will save a slightly smaller amount
   and disabling Pal2PacE will save less on top of that
  OptiPNG            http://optipng.sourceforge.net/
 
Benchmark with RHSUSAFDEV+RHSAFRFDEV+RHSGREFDEV+RHSSAFDEV:
  2m 48s pboc + python/exe version
Benchmark with RHSUSAFDEV:
  13m 58s PBOConsole + bat(ch) version
"""


class logging:
    excluded_string   = "      [Excluded]"
    del_string        = "           [DEL]"
    cd_string         = "            [CD]"
    cfgconvert_string = "    [CfgConvert]"
    mkdir_string      = "         [MKDIR]"
    unpacking_string  = " [Unpacking PBO]"
    decunting_string  = " [Decunting EBO]"


def log(log_text, log_file):
    print(log_text)
    log_file.write(log_text + "\n")


def pboc_pbo(pbo, move_dir, log_file):
    pbo_name = (pbo.split("addons")[-1])[1:]
    log(f"{logging.unpacking_string} {pbo_name}", log_file)
    subprocess.call(["pboc", "unpack", pbo],
                    cwd=move_dir,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)


def decunt_ebo(ebo, move_dir, log_file):
    ebo_name = (ebo.split("addons")[-1])[1:]
    log(f"{logging.decunting_string} {ebo_name}", log_file)
    subprocess.call(["EBODecunter", ebo],
                    cwd=move_dir,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)


def delete_pbo(pbo):
    os.remove(pbo)


def cfgconvert_export(export_folder, pbo_name, log_file):
    config = f"{export_folder}/{pbo_name}/"
    log(f"{logging.cfgconvert_string} {pbo_name}/config.bin to config.cpp", log_file)
    subprocess.call(["cfgconvert", "-txt", "-dst", "config.cpp", "config.bin"], cwd=config)
    log(f"{logging.del_string} {pbo_name}/config.bin", log_file)
    try:
        os.remove((config + "config.bin"))
    except:
        return


def export_pbo(mod, cwd, mod_name, log_file):
    # Save export folder path
    export_folder = f"{cwd}\\{mod_name}".replace("\\", "/")
    
    # Try to create the pbo export dir
    try:
        # Create dir to export pbos in
        os.mkdir(export_folder)
    except FileExistsError:
        # Folder already exists, pass
        pass

    pbo_list = glob.glob(f"{mod}/addons/*.pbo")
    for pbo in pbo_list:
        pboc_pbo(pbo, export_folder, log_file)
        pbo_name = pbo.split("addons")[1][1:-4]
        cfgconvert_export(export_folder, pbo_name, log_file)
    
    ebo_list = glob.glob(f"{mod}/addons/*.ebo")
    for ebo in ebo_list:
        decunt_ebo(ebo, export_folder, log_file)
        pbo = ebo.replace(".ebo", ".pbo")
        pboc_pbo(pbo, export_folder, log_file)
        pbo_name = pbo.split("addons")[1][1:-4]
        cfgconvert_export(export_folder, pbo_name, log_file)
        delete_pbo(pbo)


def delete_files(ext_list, path, log_file):
    # ['*.paa', '*.p3d', '*.wss', '*.ogg', '*.wav', '*.h', '*.hpp', '*.rtm', '*.bisurf']
    # C:\Users\Lukeg\Desktop\GitHub\MyRepos\Arma-Class-Exporter\ModPreperation\@RHSSAFDEV
    for root, dirs, files in os.walk(path):
        for currentFile in files:
            if currentFile.lower().endswith(ext_list) or os.stat(f"{root}/{currentFile}").st_size == 0:
                path_join = os.path.join(root, currentFile)
                path_join_formatted = "@" + (path_join.split("@"))[-1]
                log(f"{logging.del_string} {path_join_formatted}", log_file)
                os.remove(path_join)


def main():
    # cwd = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    cwd = os.path.dirname(sys.argv[0]).replace("\\", "/")

    if sys.argv[1]:
        for mod_path in sys.argv[1:]:
            try:
                mod_split = re.split(r"@", mod_path)[-1]
                if len(mod_split) >= 1:
                    raise IndexError 
                mod_name = "@" + mod_split
                print(f"Mod name = {mod_name}")
            except IndexError:
                mod_name = re.split(r"\\", mod_path)[-1]
                print(f"Mod name = {mod_name}")

            log_start_date = datetime.utcnow()
            log_start_date_string = str(log_start_date).replace(":", "-")
            #os.system(f"mkdir {cwd}/Logs > nul 2> nul")

            try:
                os.mkdir(f"{cwd}/Logs")
            except FileExistsError:
                pass

            with open(f"{cwd}/Logs/LOG - {mod_name} [{log_start_date_string}].txt", "a") as log_file:
                export_pbo(mod_path, cwd, mod_name, log_file)
                #delete_files((".paa", ".p3d", ".wss",
                #              ".ogg", ".wav", ".h",
                #              ".hpp", ".rtm", ".bisurf",
                #              ".json", ".rvmat", ".bin",
                #              ".psd", ".obj"), f"{cwd}\\{mod_name}", log_file)
    else:
        input("You need to pass a folder to this script\nPress ENTER To Exit")
    input("Press ENTER To Exit")


if __name__ == "__main__":
    main()
