from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir

# fazer auth do google drive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 
FOLDER_ID = ""
FILE_DIR = ""


# def google_drive_auth():
# 	print('a')


get_files = listdir(FILE_DIR)
print(FILE_DIR+"/"+get_files[0])
def upload_files(file_list):
	for file in file_list:

		gfile = drive.CreateFile({'parents': [{'id': FOLDER_ID}]})
		gfile.SetContentFile(file)
		gfile.Upload() # Upload the file.

def delete_all_files():
	file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1QBoUzGejJJQroUViMAqSaC0M2iZRI-7L')}).GetList()
	for file in file_list:
		file.Delete()

upload_files(FILE_DIR+"/"+get_files[0])

# vigiar pasta do morrowind pra sempre upar os arquivos
# toda vez que morrowind abrir baixar os saves novos

