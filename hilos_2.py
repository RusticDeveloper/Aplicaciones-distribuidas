from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any

class mi_hilo(threading.Thread):
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)
    def run(self):
        print(str(self.__x))


for i in range(10):
    mi_hilo(i+1).start()

