#!python3
import os
import wget
import time
import zipfile


def main():
    # setting the variables
    username = os.getenv('username')
    src_url = "https://github.com/MWSE/MWSE/releases/download/build-automatic/mwse.zip"
    dst_dir = 'C:\\Users\\' + username + '\\Downloads\\mwse.zip'

    # downloading the update
    print("Downloading the latest MWSE release..")
    print()
    wget.download(src_url, dst_dir)

    time.sleep(1)
    print()
    print()
    print("Unpacking archive..")
    time.sleep(1)

    # unzipping the update into the Morrowind directory
    with zipfile.ZipFile(dst_dir, 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())

    time.sleep(1)
    print()
    print("Removing temporary files..")
    time.sleep(1)

    # removing the temp archive
    if os.path.isfile(dst_dir):
        os.remove(dst_dir)
    else:
        pass

    time.sleep(1)
    print()
    print("Update successful!")
    time.sleep(1)


main()
