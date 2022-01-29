import os
import sys
import magic
import stat
import shutil


def move(folder_src):
    for filename in os.listdir(folder_to_track):

        filename_path = folder_src + '/' + filename

        file_stats = os.stat(filename_path)

        if stat.S_ISDIR(file_stats[stat.ST_MODE]):
            print("This is directory" + filename)
            continue

        # Search type mims of file
        type_mime = magic.Magic(mime=True, uncompress=True)
        type_file = type_mime.from_file(filename_path)

        extension_file = os.path.split(type_file)[1]

        folder = folder_to_track + "/" + "Dossier_" + extension_file

        # If folder exist insert
        # sinon create the folder and insert
        if os.path.isdir(folder):
            src = folder_src + "/" + filename
            new_destination = folder + "/" + filename
            shutil.move(src, new_destination)
        else:
            # create Directory
            path = os.path.join(folder_src, folder)
            print(path)
            os.mkdir(path)
            src = folder_src + "/" + filename
            new_destination = path + "/" + filename
            shutil.move(src, new_destination)


if len(sys.argv) == 1:
    print("Missing argument")
else:
    folder_to_track = sys.argv[1]
    move(folder_to_track)
