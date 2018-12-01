from gpiozero import PWMOutputDevice

class Motor:
    def __init__(self):
        PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
        PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive
        PWM_FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
        PWM_REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive
        self.forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)#frequency = 1000hz
        self.reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)
        self.forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
        self.reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

    def driver(f_left, r_left, f_right, r_right, self):
        self.forwardLeft.value = f_left
        self.reverseLeft.value = r_left
        self.forwardRight.value = f_right
        self.reverseRight.value = r_right 
    
    def allStop(self):
        self.driver(0, 0, 0, 0)
    
    def forwardDrive(self):
        self.driver(1.0, 0, 1.0, 0)
    
    def reverseDrive(self):
        self.driver(0, 1.0, 0, 1.0)
    
    def spinLeft(self):
        self.driver(0, 1.0, 1.0, 0)
    
    def SpinRight(self):
        self.driver(1.0, 0, 0, 1.0)
    
    def forwardTurnLeft(self):
        self.driver(0.2, 0, 0.8, 0)
    
    def forwardTurnRight(self):
        self.driver(0.8, 0, 0.2, 0)
    
    def reverseTurnLeft(self):
        self.driver(0, 0.2, 0, 0.8)
    
    def reverseTurnRight(self):
        self.driver(0, 0.8, 0, 0.2)