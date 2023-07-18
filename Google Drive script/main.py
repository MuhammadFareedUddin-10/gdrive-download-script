from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
drive = GoogleDrive(gauth)


folder = '1mAUkBFh0iVicSqAv8tLq_ID1qzrs0Kjj'


# Download files
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])










#file1 = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : 'hello2.txt'})
#file1.SetContentString('Hello world!, this is my second file')
#file1.Upload()