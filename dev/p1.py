import json
import logging
import time
from filelock import Timeout, FileLock
import sys

def writeJson(fieldname):
    data=[]
    lock = FileLock("data.json.lock")
    with lock:
        with open('data.json') as json_file:  
            data = json.load(json_file)
        cnum=data["info"][0][fieldname]
        data["info"][0][fieldname]=int(cnum)+1
        with open('data.json', 'w') as outfile:  
            json.dump(data, outfile)


field = str(sys.argv[1]) 
seconds = int(sys.argv[2])
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    
    for idx in range(100):
        writeJson(field);
        print("idx",idx)
        time.sleep(seconds)

    
    
    