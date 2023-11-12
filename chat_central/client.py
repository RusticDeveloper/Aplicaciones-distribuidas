'''
Este codigo crea un cliente que se conectara al servidor 
el cliente se puede cominicar con otros a traves del servidor
'''

# importacion de librerias necesarias
import socket,threading
# obtiene el nombre del cliente y declara la direccion y puerto del servidor
nombre=input("Ingresa tu nombre: ")
direccion='127.0.0.1'
puerto=65530
# crea un socket para el cliente y lo conecta con el servidor
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((direccion,puerto))
# esta funcion gestiona la recepcion de mensajes del servidor
def receive_msg():
    while True:
        try:
            # recive la solicitud del nombre de usuario y envia el nombre de usuario al servidor
            message=client.recv(1024).decode()
            if message == "username":
                client.send(nombre.encode())
            else:
                # imprime los mensajes enviados de otros clientes a traves del servidor
                print(message)   
        except:
            # si hay un error lo muestra y cierra la conexion con el cliente
            print("ocurrio un error")
            client.close()
            break
            
# esta funcion gestiona el envio de mensajes del cliente al servidor
def write_msg():
    while True:
        # espera el ingreso de un mensaje t lo envia al servidor
        message=f"{nombre}: {input('')}"
        client.send(message.encode())
            
# se crean hilos para gestionar la recepcion y envio de mensajes al servidor para cada cliente
receive_thread=threading.Thread(target=receive_msg)
receive_thread.start()

receive_thread=threading.Thread(target=write_msg)
receive_thread.start()