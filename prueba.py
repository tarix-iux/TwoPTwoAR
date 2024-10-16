from Motor import Motor
import time  # Importar la librería time para gestionar los tiempos

if __name__ == "__main__":
    # Inicializa el motor con los pines correspondientes
    motor = Motor(pin1=5, pin2=6, pwm_pin=12)

    # Establece la velocidad al 10%
    motor.set_speed(20)  # Establece la velocidad a 10%

    try:
        while True:
            # Establecer dirección a "forward"
            motor.set_direction("forward")
            print("Dirección: forward")
            time.sleep(3)  # Espera 3 segundos
            
            # Establecer dirección a "back"
            motor.set_direction("back")
            print("Dirección: back")
            time.sleep(3)  # Espera 3 segundos

    except KeyboardInterrupt:
        print("Deteniendo el motor...")
        motor.set_direction("none")  # Detener el motor
        GPIO.cleanup()  # Limpiar GPIO para liberar los pines
