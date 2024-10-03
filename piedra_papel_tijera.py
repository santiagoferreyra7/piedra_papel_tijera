import random
import getpass  # Para ocultar la entrada del jugador

# Clase base que explica el juego
class Juego:
    def __init__(self):
        self.movimientos = ['Piedra', 'Papel', 'Tijera']
        self.reglas = {
            'Piedra': 'Tijera',
            'Papel': 'Piedra',
            'Tijera': 'Papel'
        }
    
    def mostrar_reglas(self):
        print("Reglas del juego:")
        print("Piedra le gana a Tijera")
        print("Tijera le gana a Papel")
        print("Papel le gana a Piedra")

    def determinar_ganador(self, jugador1, jugador2):
        if jugador1 == jugador2:
            return "Empataron"
        elif self.reglas[jugador1] == jugador2:
            return "Jugador 1 ganó"
        else:
            return "Jugador 2 ganó"

# Clase que hereda de Juego para jugar contra la computadora
class JuegoConCompu(Juego):  # Herencia
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base

    def jugar(self):
        self.mostrar_reglas()
        try:
            movimiento_jugador = input("Elige: Piedra, Papel o Tijera: ").capitalize()
            if movimiento_jugador not in self.movimientos:
                raise ValueError("Movimiento no válido. Intenta de nuevo.")
            
            movimiento_compu = random.choice(self.movimientos)
            print(f"La computadora elige: {movimiento_compu}")
            
            resultado = self.determinar_ganador(movimiento_jugador, movimiento_compu)
            print(resultado)
        except ValueError as e:
            print(e)

# Clase que hereda de Juego para jugar entre dos jugadores
class JuegoConPibe(Juego):  # Herencia
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base

    def jugar(self):
        self.mostrar_reglas()
        try:
            movimiento_jugador1_input = getpass.getpass("Jugador 1, elige: 'z' para Piedra, 'x' para Papel, 'c' para Tijera: ").lower()
            movimiento_jugador1 = self.validar_movimiento(movimiento_jugador1_input)

            movimiento_jugador2_input = getpass.getpass("Jugador 2, elige: '1' para Piedra, '2' para Papel, '3' para Tijera: ")
            movimiento_jugador2 = self.validar_movimiento(movimiento_jugador2_input, es_jugador2=True)

            print("\nJugador 1 eligió:", movimiento_jugador1)
            print("Jugador 2 eligió:", movimiento_jugador2)
            resultado = self.determinar_ganador(movimiento_jugador1, movimiento_jugador2)
            print(resultado)
        except ValueError as e:
            print(e)

    def validar_movimiento(self, movimiento_input, es_jugador2=False):
        if es_jugador2:
            opciones = {'1': 'Piedra', '2': 'Papel', '3': 'Tijera'}
        else:
            opciones = {'z': 'Piedra', 'x': 'Papel', 'c': 'Tijera'}
        
        if movimiento_input in opciones:
            return opciones[movimiento_input]
        else:
            raise ValueError("Movimiento no válido. Intenta de nuevo.")

# Función principal para ejecutar el juego
def main():
    print("Bienvenido al Piedra, Papel y Tijera!")
    modo = input("Elegí el modo de juego: 'compu' para jugar contra la computadora, 'pibe' para jugar entre dos jugadores: ").lower()
    
    try:
        if modo == 'compu':
            juego = JuegoConCompu()
            juego.jugar()
        elif modo == 'pibe':
            juego = JuegoConPibe()
            juego.jugar()
        else:
            raise ValueError("Opción no válida. Por favor, elige 'compu' o 'pibe'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
