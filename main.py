from functions import FileService
import sys
from time import sleep
from constant import *

def read_options():
    file_service = FileService()
    print("Bienvenido al sistema de validación de datos")
    opt = int(input("Ingrese una opción: "))
    options = {
        0: sys.exit,
        1: file_service.get_all_user_sessions,
        2: file_service.get_sessions_by_user_and_date,
        3: file_service.sesion_time,
        4: file_service.get_macs_by_user,
        5: file_service.get_users_by_macap_and_date,
    }
    if opt in options:
        options[opt]()
    else:
        print("Opción inválida")
        sleep(2)
        read_options()

if __name__ == '__main__':
    while True:
        print(MAIN)
        print(read_options())
        sleep(2)

