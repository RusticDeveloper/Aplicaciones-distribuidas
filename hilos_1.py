import threading,time
def hola_mundo(nombre):
    print("Hello world, saludos " + nombre)
    time.sleep(5)

if __name__ == '__main__':
    
    thread = threading.Thread(target=hola_mundo,args=("Daniel",))
    thread.start()
    thread.join()

    print("este codigo se ejecutara primero, por que esta en el hilo principal, excepto cuando se usas el metodo join")
