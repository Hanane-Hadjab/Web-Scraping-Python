import os
import magic
import stat
import shutil
import argparse


def move(folder_src, extension_arg):
    for filename in os.listdir(folder_src):

        filename_path = folder_src + '/' + filename
        file_stats = os.stat(filename_path)

        if stat.S_ISDIR(file_stats[stat.ST_MODE]):
            print(filename + " is a directory")
            continue

        if extension_arg is None:
            # Search type mims of file
            type_mime = magic.Magic(mime=True, uncompress=True)
            type_file = type_mime.from_file(filename_path)  # exemple application/pdf
            extension_file = os.path.split(type_file)[1]  # exemple pdf
        else:
            extension_file = extension_arg

        folder = folder_src + "/" + "Dossier_" + extension_file

        # If folder exist  then insert file in it
        if os.path.isdir(folder):
            if extension_arg is not None:
                if filename.endswith('.'+extension_arg):
                    src = folder_src + "/" + filename
                    new_destination = folder + "/" + filename
                    shutil.move(src, new_destination)
            else:
                src = folder_src + "/" + filename
                new_destination = folder + "/" + filename
                shutil.move(src, new_destination)
        else:
            # sinon create the folder and insert
            # create Directory
            path = os.path.join(folder_src, folder)
            if extension_arg is not None:
                if filename.endswith('.'+extension_arg):
                    os.mkdir(path)
                    src = folder_src + "/" + filename
                    new_destination = path + "/" + filename
                    shutil.move(src, new_destination)
            else:
                os.mkdir(path)
                src = folder_src + "/" + filename
                new_destination = path + "/" + filename
                shutil.move(src, new_destination)


parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True, help="Le chemin de dossier cible")
parser.add_argument('--only', type=str, help='L extension de fichier a rangé ')
args = parser.parse_args()

move(args.path, args.only)
