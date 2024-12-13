import time
import random

def timer(function):
    def medir_funcion():
        inicio = time.time()
        function()
        fin = time.time()
        print(fin-inicio)
    return medir_funcion

@timer
def cita():
    return random.random()

cita()