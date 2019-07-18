from lockwrite import RWLock
import time
import sys
import logging
import json
import random

rwlock=RWLock("data.json")
excTime=0.0
loops=int(sys.argv[1])
fields=["dp1","dp2","dp3"]

def main():
    excTime=0
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
        
        time.sleep(0.001)
    return excTime/loops;
    

if __name__ == "__main__":
    timeExc=main()
    print(timeExc)
    