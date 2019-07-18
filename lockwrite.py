from filelock import Timeout, FileLock

class RWLock:
    # Constructor recibe el nombre del archivo
    def __init__(self, file):
        self.file = file # almacena el nombre del archivo
        self.filelock = str(file)+".lock" # crea el lock del archivo
        self.lock =  FileLock(self.filelock) 
        self.persitentLock=False # variable que permite tener un lock al leer y liberarlo cuando se termine de escribir

    # Lectura insegura o normal de un archivo
    def uread(self): 
        file=open(self.file, "r")
        data=file.read()
        file.close()
        return data
    
    # Escritura insegura o normal de un archivo
    def uwrite(self,data):
        file=open(self.file, "w")
        file.write(data)
        file.close()

    # Lectura segura de un archivo
    def read(self,lck=False): 
        data=""
        # Lock persistente
        if(lck):
            self.lock.acquire(timeout=10) # Creo el lock y designo que se terminara en 10 segundos
            try:
                data=self.uread() # Leo el archivo
                self.persitentLock=True # Indico que ese lock se quedara esperando a escribir
            except:
                self.persitentLock=False # Si la lectura falla libero el lock
                self.lock.release()
        # Sin lock persistente
        else:
            with self.lock: # Creo un lock temporal para leer el archivo
                data=self.uread()
        return data 

    # Escritura segura de un archivo
    def write(self,data):
        if(self.persitentLock): # Si tengo un lock persistente
            self.uwrite(data) # Escribo el archivo
            self.lock.release() # Libero el lock
        else: # Sin lock persistente
            with self.lock: # Creo un lock temporal para escribir el archivo
                self.uwrite(data) # Escribo el archivo
