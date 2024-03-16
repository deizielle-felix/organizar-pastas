import os
import shutil


dir_dest = {'Imagens': ['.jpg', '.png', '.svg'],
             'Vídeos': ['.mp4'],
             'PDF': ['.pdf']
             }

user = os.environ['USERNAME']
path = f"/home/{user}/Downloads" # caminho para a pasta desorganizada
archives_dir = os.listdir(path=path)

for archive in archives_dir:
    for directory, file_type in dir_dest.items():
        if any(ext in archive for ext in file_type):
            destination = f'/home/{user}/{directory}'
            origin = f'{path}/{archive}'
            shutil.move(origin, destination)

