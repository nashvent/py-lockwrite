# ShellCatch
# Issue CMF-39
Bloqueo de escritura de archivos Json
* file name: lockwrite.py
* class name: RWLock
### Instanciar
```
from lockwrite import RWLock    # importar modulo
rwlock=RWLock("data.json")      # instanciar clase indicando el archivo
```
### Leer
```
 data = rwlock.read() # Lee el archivo y retorna un string

 data = rwlock.read(True) # Lee el archivo, retorna un string y protege al archivo hasta que se escriba
```

### Escribir
```
 rwlock.write(data) # Recibe un string y escribre el archivo, libera el lock en caso se haya usado rwlock.read(True)
```
## Test
Para probar el funcionamiento correr el archivo de test.py
```
 python3 test.py $loops   # la variable loops indica las veces que quiere escribir el archivo
```


# Issue CMF-40
El script devuelve el tiempo promedio
```
./runCMF-40.sh $loops 
```