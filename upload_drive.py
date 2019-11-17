from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from tqdm import tqdm

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)
parent_folder_name='html_storage'

print('loading all files directory...')
files = sorted(list(os.listdir(parent_folder_name)))
print('done')
print('start uploading files')
for i in tqdm(range(len(files))):
    filename = files[i]
    if filename[-4:] == 'html':
        cnt = 0
        while True:
            try:
                with open(os.path.join(parent_folder_name,filename), "r") as f:
                    file_drive = drive.CreateFile({'title':os.path.basename(f.name), 'parents':[{'id': '1xS4isTv1MQBVmFT1BDbGyS0e1i5_mss2'}] })
                    file_drive.SetContentString(f.read()) 
                    file_drive.Upload()
                    # print('done uploading', filename)
                    #garbage collect
                    del file_drive
                    break
            except:
                print('upload failed on ',filename)
                cnt += 1
                if cnt > 3:
                    cnt = 0
                    break
