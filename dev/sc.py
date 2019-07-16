import json
import threading
import logging
import time
from filelock import Timeout, FileLock
import random



# data['info'] = []  
# data['info'].append({  
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# # Read
# with open('data.json') as json_file:  
#     data = json.load(json_file)
#     print (data["info"])

# #Write
# with open('data.json', 'w') as outfile:  
#     json.dump(data, outfile)


fields=["name","website","from"]
threads=[None]*len(fields)
#rnum=random.randint(1,101)

def writeJson(fieldname,rnum):
    data=[]
    lock = FileLock("data.json.lock")
    with lock:
        with open('data.json') as json_file:  
            data = json.load(json_file)
        data["info"][0][fieldname]=fieldname+str(rnum)
        with open('data.json', 'w') as outfile:  
            json.dump(data, outfile)


# def thread_function(name,rnum):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     writeJson(name,rnum)
#     logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    
    for fld in range(len(fields)):
        threads[fld] = threading.Thread(target=writeJson, args=(fields[fld],3))
        threads[fld].start()
    
    #y = threading.Thread(target=thread_function, args=(2,))
    #y.start()
    # x.join()
    logging.info("Main    : all done")