import json
import logging
import time
from filelock import Timeout, FileLock
import sys



class RWLock:
    def __init__(self, file):
        self.file = file
        self.filelock = str(file)+".lock"
        self.lock =  FileLock(self.filelock)
        self.persitentLock=False

    def uread(self):
        file=open(self.file, "r")
        data=file.read()
        file.close()
        return data
    
    def uwrite(self,data):
        file=open(self.file, "w")
        file.write(data)
        file.close()

    def read(self,lck=False): #lck (false) es lectura segura, lck(True) es lectura que necesita de un write obligatoriamente
        data=""
        if(lck):
            self.lock.acquire(timeout=10)
            try:
                data=self.uread()
                self.persitentLock=True
            except:
                self.persitentLock=False
                self.lock.release()
        else:
            with self.lock:
                data=self.uread()
        return data


    def write(self,data):
        if(self.persitentLock):
            self.uwrite(data)
            self.lock.release()
        else:
            with self.lock:
                self.uwrite(data)


# def writeJson(fieldname):
#     data=[]
#     lock = FileLock("data.json.lock")
#     with lock:
#         with open('data.json') as json_file:  
#             data = json.load(json_file)
#         cnum=data["info"][0][fieldname]
#         data["info"][0][fieldname]=int(cnum)+1
#         with open('data.json', 'w') as outfile:  
#             json.dump(data, outfile)


# field = str(sys.argv[1]) 
# seconds = int(sys.argv[2])
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    
#     for idx in range(100):
#         writeJson(field);
#         print("idx",idx)
#         time.sleep(seconds)

    
    
    