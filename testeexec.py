import os
import dropbox

def upload_to_dropbox(folder_path, access_token):
    dbx = dropbox.Dropbox(access_token)

    # Lista todos os arquivos na pasta
    files = os.listdir(folder_path)

    # Faz o upload de cada arquivo para o Dropbox
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # Verifica se é um arquivo
            with open(file_path, "rb") as f:
                dbx.files_upload(f.read(), "/" + file_name)
            print(f"Arquivo '{file_name}' enviado para o Dropbox com sucesso.")

if __name__ == "__main__":
    # Caminho para a pasta onde o arquivo Python está sendo executado
    current_dir = os.getcwd()
    
    # Token de acesso gerado para o aplicativo Dropbox
    access_token = "sl.BznF_aGLwCXQ9H6LvMWA7CONPmzwFgCFQHKDfc4oGmyjdnW-BQFqOLd6NvJy-MkgW0u7E-B4cOEZ1Ebwz6M1hQhkD5oa-P2NADLTqEuoaB-MK2vAKebQ04wPct_DrTmZG_ucm8uzVWz_"

    upload_to_dropbox(current_dir, access_token)
