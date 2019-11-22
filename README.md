# Pantip-Scraper
Pantip scraper using rendertron (headless Chrome)

Pantip website changes it's api too constantly, rendering old web scraper to not work properly after some period of time. So the best web scraper should be operating on the headless browser. 

# How to
- git clone <repo> && cd <this folder>
- npm install rendertron
- rendertron
  
# For scraping

usage: `python3 scrape.py [-h] [-o OVERWRITE] [-a ALL] [-v VERBOSE] [-w WORKERS] range a b`


remark: a and b must be in between [30000000, latest_topic_id]

positional arguments:

- range         scrape the website given tid range [a,b]

optional arguments:

- -h, --help          [show this help message and exit]
  
- -o OVERWRITE, --overwrite OVERWRITE         [enable overwrite all existing storage files]
                        
- -a ALL, --all ALL         [scrap all tids (approx 9 mil.)]
  
- -v VERBOSE, --verbose VERBOSE         [enable verbosity]
                        
- -w WORKERS, --workers WORKERS         [number of workers (multiprocessing)]


# For converting HTML to useful data


run: `python3 convert.py ...` (undone)

