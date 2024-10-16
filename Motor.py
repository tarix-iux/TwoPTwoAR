import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pin1, pin2, pwm_pin, freq_ms=100):
        self.PinPWM = pwm_pin
        self.Pin1 = pin1
        self.Pin2 = pin2
        self.Freq_ms = freq_ms
        self.Speed = 10
        self.Direction = 'none'

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PinPWM, GPIO.OUT)
        GPIO.setup(self.Pin1, GPIO.OUT)
        GPIO.setup(self.Pin2, GPIO.OUT)

        self.PWM = GPIO.PWM(self.PinPWM, self.Freq_ms)
        self.PWM.start(self.Speed)

        GPIO.output(self.Pin1, GPIO.LOW)
        GPIO.output(self.Pin2, GPIO.LOW)

    def set_speed(self, speed):
        if 0 <= speed <= 100:
            self.Speed = speed
            self.PWM.ChangeDutyCycle(self.Speed)
        else:
            raise ValueError("Speed must be between 0 and 100")

    def set_direction(self, direction):
        if direction == 'forward':
            self.Direction = 'forward'
            GPIO.output(self.Pin1, GPIO.HIGH)
            GPIO.output(self.Pin2, GPIO.LOW)
        elif direction == 'back':
            self.Direction = 'back'
            GPIO.output(self.Pin1, GPIO.LOW)
            GPIO.output(self.Pin2, GPIO.HIGH)
        elif direction == 'none':
            GPIO.output(self.Pin1, GPIO.LOW)
            GPIO.output(self.Pin2, GPIO.LOW)
        else:
            return "Error: Invalid Direction"
        
        return "Ok"
        
    def __repr__(self):
        return f"Motor(pin1={self.Pin1}, pin2={self.Pin2}, pwm_pin={self.PinPWM}, direction='{self.Direction}', speed={self.Speed})"
    
    def __str__(self):
        return "Clase Motor"
