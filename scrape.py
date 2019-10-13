import requests
import os

tid = 30000000
SERVER_BASE_URL = '0.0.0.0'
PORT = '3000'
MODE = 'render'

r = requests.get(f'http://{SERVER_BASE_URL}:{PORT}/{MODE}/http://www.pantip.com/topic/{tid}')

print('status code returned',r.status_code)

with open(os.path.join('html_storage',f'{tid}.html'),'w') as f:
    #save file
    f.writelines(r.text)
