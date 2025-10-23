#./object/mascota.py

#Creo mi objeto por medio de una clase llamada "mascota"
class Mascota:
    #Creamos nuestro constructor para la mascota, definiendo sus estados bases
    def __init__(self):
        self.nombre = ""
        self.nombrar_mascota()
        self.energia = 100
        self.comida = 100
        self.animo = 0
    
    #Se crea el metodo para nombrar a la mascota
    def nombrar_mascota(self):
        print("\n" + "═" * 50)
        print("🎮  Bienvenido a Cat Simulator!  🎮".center(50))
        print("═" * 50 + "\n")
        self.nombre = input("Por favor, ingrese el nombre de tu gato 😺: ")
        print(f"\n✨ ¡Excelente elección! Tu compañero {self.nombre} está listo para comenzar su aventura. 🐾")
        input("\nPresione ENTER para continuar...")
    
    #Creamos nuestro metodo de alimentar
    def alimentar(self):
        #Establecemos el limite de mis estados de comida y energia para no sobrepar los estados establecidos
        if self.comida == 100 or self.energia == 100:
            return f"{self.nombre} no quiere comer más 😒, tiene la panza llena o tiene mucha energia."
        else:
            self.energia = min(self.energia + 20, 100)
            self.comida = min(self.comida + 20, 100)
            return f"{self.nombre} comió 🥩 y está feliz!"
    
    #Del mismo modo, realizaremos nuestros demas metodos
    def descansar(self):
        if self.energia == 100:
            return f"{self.nombre} tiene mucha energia! 😐, no puede normir!."
        else:
            self.energia = min(self.energia + 20, 100)
            self.comida = max(self.comida - 10, 0)
            self.animo = min(self.animo + 5, 100)
            return f"{self.nombre} descansó 🛌 y se siente mejor."
            
    def jugar(self):
        if self.energia < 20 or self.comida < 20:
            self.animo = max(self.animo - 10, 0)
            return f"{self.nombre} está demasiado cansado o hambriento 😩 para jugar."
        else:
            self.energia = max(self.energia - 30, 0)
            self.comida = max(self.comida - 20, 0)
            self.animo = min(self.animo + 30, 100)
            return f"{self.nombre} jugó 🎾 y está feliz!"

    
    #Creamos nuestro metodo para crear las barras, a dicho metodo le pasaremos nuestros puntos de estado junto
    #con el largo que queremos que tenga nuestro barra
    def barra_estado(self, valor, largo=10):
        #creamos la operacion para determinar la cantidad de bloques de la barra
        bloques = int((valor / 100) * largo)
        #establecemos el espacio que tendra nuestra barra
        vacios = largo - bloques
        
        #Creamos una serie de condicionales para determinar el color de las barras de estado
        if valor >= 70:
            color = "\033[92m"  # verde
        elif valor >= 40:
            color = "\033[93m"  # amarillo
        else:
            color = "\033[91m"  # rojo
        reset = "\033[0m"
        
        #retornamos utilizando codigo ASCII
        return f"{color}[{'█' * bloques}{' ' * vacios}] {valor:3d}%{reset}"
    
    def mostrar_estado(self):
        width = 64
        nombre_mostrado = self.nombre
        # Limitar nombre si es muy largo
        if len(nombre_mostrado) > 20:
            nombre_mostrado = nombre_mostrado[:17] + "..."

        # Cabecera decorativa
        print(" " * 8 + "╔" + "═" * width + "╗")
        print(" " * 8 + "║" + "🐾 ESTADO DE TU MASCOTA 🐾".center(width) + "║")
        print(" " * 8 + "╚" + "═" * width + "╝")

        # Cuerpo del estado
        print(" " * 8 + "╔" + "═" * width + "╗")
        print(" " * 8 + "║" + f"Nombre : {nombre_mostrado}".ljust(width) + "║")
        print(" " * 8 + "║" + f"Energía: {self.barra_estado(self.energia)}".ljust(width) + "║")
        print(" " * 8 + "║" + f"Comida : {self.barra_estado(self.comida)}".ljust(width) + "║")
        print(" " * 8 + "║" + f"Ánimo  : {self.barra_estado(self.animo)}".ljust(width) + "║")
        print(" " * 8 + "╚" + "═" * width + "╝\n")