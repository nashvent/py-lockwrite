from lockwrite import RWLock
import time
import sys
import logging
import json
import random


loops=int(sys.argv[1])

def main():
    excTime=0.0
    rwlocks=[]
    for nlocks in range(2):
        rwlocks.append(RWLock("data_test/data"+str(nlocks+1)+".json"))    

    for idx in range(loops):
        for nlocks in range(2):
            rwlock=rwlocks[nlocks]
            start = time.time()
            data=rwlock.read(True)
            ##Json 
            jdata=json.loads(data)
            rnum=random.randint(1,10)
            rfield="dp"+str(rnum)
            cnum=jdata["info"][0][str(rfield)]
            jdata["info"][0][rfield]=int(cnum)+1+idx
            data=json.dumps(jdata, ensure_ascii=False)
            #EndJson
            rwlock.write(data)
            end = time.time()
            excTime+=(end - start)
        time.sleep(0.001)
    return excTime/(loops*2);
    
if __name__ == "__main__":
    print("tiempo:",main())