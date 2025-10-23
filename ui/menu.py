#./ui/menu.py
#Importamos nuestro objeto
from object.mascota import Mascota
#Impostamos OS para realizar la limpieza de nuestro termina
import os

#Creamos nuestra clase menu
class Menu:
    #Creamos un constructor para "inyectar" nuestro objeto
    def __init__(self):
        self.mascota = Mascota()
    
    #Establecemos nuestro metodo para limpiar la terminal
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    #Creamoes nuestro metodo de menu
    def mostrar_menu(self):
        while True:
            #Limpiamos la pantalla despues de ejecutar cualquier opcion
            self.limpiar_pantalla()
            
            print("\n" * 2)

            #Mostramos el estado de nuestra mascota
            self.mascota.mostrar_estado()
            
            width = 64
            print(" " * 8 + "╔" + "═" * width + "╗")
            print(" " * 8 + "║" + "⚔️  MENÚ RPG ⚔️".center(width) + "║")
            print(" " * 8 + "╠" + "═" * width + "╣")
            print(" " * 8 + "║" + "[1] 🍖 Alimentar".ljust(width) + "║")
            print(" " * 8 + "║" + "[2] ⚽ Jugar".ljust(width) + "║")
            print(" " * 8 + "║" + "[3] 💤 Descansar".ljust(width) + "║")
            print(" " * 8 + "║" + "[4] 🚪 Salir".ljust(width) + "║")
            print(" " * 8 + "╚" + "═" * width + "╝")

            opcion = input("Seleccione una opción: ").strip()

            #Por medio de los siguientes condicionales establecemos la accion que ejecutara el menu
            if opcion == "1":
                mensaje = self.mascota.alimentar()
            elif opcion == "2":
                mensaje = self.mascota.jugar()
            elif opcion == "3":
                mensaje = self.mascota.descansar()
            elif opcion == "4":
                self.limpiar_pantalla()
                print(f"¡Hasta pronto, {self.mascota.nombre}!")
                break
            else:
                mensaje = "Opción no válida, intente de nuevo."

            #Mostrar mensaje y pausar antes de refrescar
            print(f"\n{mensaje}")
            input("\nPresione ENTER para continuar...")