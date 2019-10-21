import requests
import os
from multiprocessing import Pool, TimeoutError
import time
import argparse

start_tid,end_tid = 30000000,30000001
SERVER_BASE_URL = '0.0.0.0'
PORT = '3000'
MODE = 'render'
verbose = False
overwrite = False
k = 10
visited = set()

def scrape(tid):
    if tid in visited:
        if overwrite:
            if verbose:
                print(f'overwriting {tid}')
        else:
            if verbose:
                print(f'skipping {tid} as it alredy exists')
            return

    r = requests.get(f'http://{SERVER_BASE_URL}:{PORT}/{MODE}/http://www.pantip.com/topic/{tid}')
    ERROR_CODE = r.status_code
    if verbose:
        print(f'{tid}: status code returned',ERROR_CODE)
    if ERROR_CODE != 200:
        with open('log.txt','a') as f2: #not tested !!
            f2.write(f'{tid}: got weird status code return {ERROR_CODE}\n')
    with open(os.path.join('html_storage',f'{tid}.html'),'w') as f:
        #save file
        f.writelines(r.text)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Scrape the Pantip website!')
    parser.add_argument('range', nargs='?', type=int, help='scrape the website given tid range [a,b]')
    parser.add_argument('-o','--overwrite', action='store_true', help='enable overwrite all existing storage files')
    parser.add_argument('-a','--all', action='store_true', help='scrap all tids (approx 9 mil.)')
    parser.add_argument('-v','--verbose', action='store_true', help='enable verbosity (expressive mode)')
    parser.add_argument('-w','--workers', default=10, help='number of workers (multiprocessing)')

    args = parser.parse_args()
    k = int(args.workers)
    if(args.overwrite):
        overwrite = True
    if(args.all):
        end_tid = 39315577
    else:
        start_tid, end_tid = int(args.range[0]), int(args.range[1])+1
    if args.verbose:
        verbose = True
        print('verbose mode ON')
        print('worker set to',k)
        if(args.overwrite):
            print('overwrite mode ON')
        if(args.all):
            print('scraping ALL tids (this may take some time)')
    try:
        os.listdir('html_storage')
        if verbose:
            print('Found html_storage directory.')

        visited = set([int(s.split('.')[0]) for s in os.listdir('html_storage')])
    except:
        print('html_storage directory not found. Creating a new directory now')
        os.mkdir('html_storage')

    pool = Pool(processes=k) # start k worker processes
    pool.map(scrape, range(start_tid, end_tid)) #compute first k tids