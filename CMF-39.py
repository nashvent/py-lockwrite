from lockwrite import RWLock
import time
import sys
import logging
import json
import random
#field = str(sys.argv[1]) 

rwlock=RWLock("data.json")
excTime=0.0
loops=10000
fields=["dp1","dp2","dp3"]
if __name__ == "__main__":

    for idx in range(loops):
        start = time.time()
        
        data=rwlock.read(True)
        ##Json 
        jdata=json.loads(data)
        
        for idx2 in range(len(fields)):
            cnum=jdata["info"][0][fields[idx2]]
            jdata["info"][0][fields[idx2]]=int(cnum)+1+idx2
        data=json.dumps(jdata, ensure_ascii=False)
        #EndJson
        rwlock.write(data)
        end = time.time()
        excTime+=(end - start)
        
        print("idx",idx)
        time.sleep(0.001)
    print("Tiempo Promedio",excTime/loops)
# python3 test.py dp2