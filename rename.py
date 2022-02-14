import os
from os import listdir
from os.path import isfile, join
import argparse
from posixpath import split


def rename(oldName, format):
    # ffxiv_01012022_142630_753.jpg || ffxiv_01012022_142630_753.png
    splitName = oldName.split("_")
    if len(splitName) != 4:
        return None
    if len(splitName[1]) != 8:
        return None
    # examine splitName[1]
    newName = ""
    if format.lower() == "mmddyyyy":
        try:
            month = splitName[1][0:2]
            day = splitName[1][2:4]
            year = splitName[1][4:]
            newName = year + month + day
        except IndexError:
            return None
    elif format.lower() == "ddmmyyyy":
        try:
            day = splitName[1][0:2]
            month = splitName[1][2:4]
            year = splitName[1][4:]
            newName = year + month + day
        except IndexError:
            return None
    else:
        print("Unrecognised format, exiting")
        quit()
    splitName[1] = newName
    newName = "_".join(splitName)
    return newName


def main():
    parser = argparse.ArgumentParser(
        description="Processes ff14 screenshots naming format to YYYYMMDD"
    )
    parser.add_argument(
        "--path", "-p", help="the path to the screenshot folder", required=True
    )
    parser.add_argument(
        "--format",
        "-f",
        help="format screenshots are in, either ddmmyyyy or mmddyyyy",
        required=True,
    )
    args = parser.parse_args()
    files = [f for f in listdir(args.path) if isfile(join(args.path, f))]
    # print(onlyfiles)
    SEP = os.path.sep
    NEWPATH = args.path + SEP
    for file in files:
        oldfile = args.path + SEP + file
        newFileName = rename(file, args.format)
        if newFileName == None:
            continue
        newfile = NEWPATH + newFileName
        os.rename(oldfile, newfile)


if __name__ == "__main__":
    main()
