from lockwrite import RWLock
import time
import sys
import logging
import json
import random
field = str(sys.argv[1]) 
seconds = int(sys.argv[2])

rwlock=RWLock("data.json")
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    #logging.basicConfig(format=format, level=logging.INFO)
    
    for idx in range(10000):
        data=rwlock.read()
        ##Json 
        jdata=json.loads(data)
        cnum=jdata["info"][0][field]
        jdata["info"][0][field]=int(cnum)+1
        data=json.dumps(jdata, ensure_ascii=False)
        #EndJson
        rwlock.write(data)
        print("idx",idx)
        time.sleep(0.001)