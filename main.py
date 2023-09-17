import os
import shutil

# Downloads folder
original_file = '/users/francisoliveira/Downloads'

# Creating directories and giving names
image_folder = '/users/francisoliveira/Downloads/Images'
documents_folder = '/users/francisoliveira/Downloads/Documents'
videos_folder = '/users/francisoliveira/Downloads/Videos'
install_folder = '/users/francisoliveira/Downloads/Installers'

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

if not os.path.exists(documents_folder):
    os.makedirs(documents_folder)

if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

if not os.path.exists(install_folder):
    os.makedirs(install_folder)

# Checking all the files
for arquivo in os.listdir(original_file):
    caminho_arquivo = os.path.join(original_file, arquivo)

    # Checking the file and moving to the new folder
    if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        shutil.move(caminho_arquivo, os.path.join(image_folder, arquivo))
    elif arquivo.lower().endswith(('.pdf', '.doc', '.docx', '.txt', '.xlsx', '.odt')):
        shutil.move(caminho_arquivo, os.path.join(documents_folder, arquivo))
    elif arquivo.lower().endswith(('.mp4', '.avi', '.mkv')):
        shutil.move(caminho_arquivo, os.path.join(videos_folder, arquivo))
    elif arquivo.lower().endswith('.dmg'):
        os.remove(caminho_arquivo)
    elif arquivo.lower().endswith(('.exe', '.app', '.pkg', '.zip')):
        shutil.move(caminho_arquivo, os.path.join(install_folder, arquivo))
    else:

        print(f"File unknown: {arquivo}")

print("Job done!!.")

