from gpiozero import PWMOutputDevice

class Motor:
    def __init__(self):
        MOTA_PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
        MOTA_PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive

        MOTB_PWM_FORWARD_RIGHT_PIN = 6	# IN1 - Forward Drive
        MOTB_PWM_REVERSE_RIGHT_PIN = 13	# IN2 - Reverse Drive

        MOTC_PWM_FORWARD_RIGHT_PIN = 22	# IN1 - Forward Drive
        MOTC_PWM_REVERSE_RIGHT_PIN = 27	# IN2 - Reverse Drive

        MOTD_PWM_FORWARD_LEFT_PIN = 9	# IN1 - Forward Drive
        MOTD_PWM_REVERSE_LEFT_PIN = 10	# IN2 - Reverse Drive

        self.forwardLeftMotA = PWMOutputDevice(MOTA_PWM_FORWARD_LEFT_PIN, True, 0, 1000)#frequency = 1000hz
        self.reverseLeftMotA = PWMOutputDevice(MOTA_PWM_REVERSE_LEFT_PIN, True, 0, 1000)
        
        self.forwardRightMotB = PWMOutputDevice(MOTB_PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
        self.reverseRightMotB = PWMOutputDevice(MOTB_PWM_REVERSE_RIGHT_PIN, True, 0, 1000)
        
        self.forwardLeftMotC = PWMOutputDevice(MOTC_PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
        self.reverseLeftMotC = PWMOutputDevice(MOTC_PWM_REVERSE_RIGHT_PIN, True, 0, 1000)
        
        self.forwardRightMotD = PWMOutputDevice(MOTD_PWM_FORWARD_LEFT_PIN, True, 0, 1000)
        self.reverseRightMotD = PWMOutputDevice(MOTD_PWM_REVERSE_LEFT_PIN, True, 0, 1000)
    
    def allStop(self):
        self.forwardLeftMotA.value = 0
        self.reverseLeftMotA.value = 0
        
        self.forwardRightMotB.value = 0
        self.reverseRightMotB.value = 0 
        
        self.forwardLeftMotC.value = 0
        self.reverseLeftMotC.value = 0
        
        self.forwardRightMotD.value = 0
        self.reverseRightMotD.value = 0 
    
    def forwardDrive(self):
        self.forwardLeftMotA.value = 1.0
        self.reverseLeftMotA.value = 0
        
        self.forwardRightMotB.value = 1.0
        self.reverseRightMotB.value = 0 
        
        self.forwardLeftMotC.value = 1.0
        self.reverseLeftMotC.value = 0
        
        self.forwardRightMotD.value = 1.0
        self.reverseRightMotD.value = 0 
    
    def reverseDrive(self):
        self.forwardLeftMotA.value = 0
        self.reverseLeftMotA.value = 1.0
        
        self.forwardRightMotB.value = 0
        self.reverseRightMotB.value = 1.0 
        
        self.forwardLeftMotC.value = 0
        self.reverseLeftMotC.value = 1.0
        
        self.forwardRightMotD.value = 0
        self.reverseRightMotD.value = 1.0 


#motor = Motor()
#while True:
#    motor.forwardDrive()
