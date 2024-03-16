import os
import shutil


dir_dest = {'Pasta de imagens': ['.jpg', '.png', '.svg'],
             'Pasta de videos': ['mp4'],
             'Pasta de PDF': ['.pdf']}

path = 'path/para/pasta/desorganizada'
archives_dir = os.listdir(path=path)

for archive in archives_dir:
    for directory, file_type in dir_dest.items():
        if any(ext in archive for ext in file_type):
            shutil.move(f'{path}/{archive}', f'{path}/{directory}')
