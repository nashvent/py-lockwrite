import json
import logging
from filelock import Timeout, FileLock

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

    def read(self,lck=False): 
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
