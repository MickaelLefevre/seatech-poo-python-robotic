from cgitb import enable
from controller import Robot, Motor, Camera, DistanceSensor, Motion
import random

alert = 0

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)



class SeatechRobot(Robot, Camera, DistanceSensor):
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        
        self.cam = Camera('camera')
        self.cam.enable(samplingPeriod=50)
        self.cam.recognitionEnable(samplingPeriod=50)

        self.alert = 0

        self.radar0 = DistanceSensor("ps0")
        self.radar1 = DistanceSensor("ps1")
        self.radar2 = DistanceSensor("ps2")
        self.radar3 = DistanceSensor("ps3")
        self.radar4 = DistanceSensor("ps4")
        self.radar5 = DistanceSensor("ps5")
        self.radar6 = DistanceSensor("ps6")
        self.radar7 = DistanceSensor("ps7")

        self.radar0.enable(samplingPeriod=50)
        self.radar1.enable(samplingPeriod=50)
        self.radar2.enable(samplingPeriod=50)
        self.radar3.enable(samplingPeriod=50)
        self.radar4.enable(samplingPeriod=50)
        self.radar5.enable(samplingPeriod=50)
        self.radar6.enable(samplingPeriod=50)
        self.radar7.enable(samplingPeriod=50)

        

    def turn(self,angle):
        if angle < 0:
            self.__leftMotor.setVelocity(- MAX_SPEED)
            self.__rightMotor.setVelocity(MAX_SPEED)
        if angle > 0:           
            self.__leftMotor.setVelocity(MAX_SPEED)
            self.__rightMotor.setVelocity( - MAX_SPEED) 

    def reperrage(self):
        self.alert = 0
        objs = self.cam.getRecognitionObjects()
        if len(objs) == 0:
            print('OK')
           
        for obj in objs:
            if obj.get_colors() == [1.0, 1.0, 1.0, 0.0, 0.0, 0.0]:
                print('Alerte')
                 
                self.alert = 1  
            else:
                print('OK')
                

    def run_away(self):
        if self.alert == 1:
            self.__leftMotor.setVelocity(-MAX_SPEED)
            self.__rightMotor.setVelocity(-MAX_SPEED)
    
    def radar_recul(self):
        surface0 = self.radar0.getValue()/4096
        surface1 = self.radar1.getValue()/4096
        surface2 = self.radar2.getValue()/4096
        surface3 = self.radar3.getValue()/4096
        surface4 = self.radar4.getValue()/4096
        surface5 = self.radar5.getValue()/4096
        surface6 = self.radar6.getValue()/4096
        surface7 = self.radar7.getValue()/4096

        print("Avant droit :   ", surface0)
        print("Droit avant :   ", surface1)
        print("Droit :         ", surface2)
        print("Arrière droit : ", surface3)
        print("Arrière gauche :", surface4)
        print("Gauche :        ", surface5)
        print("Gauche avant :  ", surface6)
        print("Avant gauche :  ", surface7)
        print("----------------------------------")

        surface_proche = max(surface0,surface1,surface2,surface3,surface4,surface5,surface6,surface7)
        print(surface_proche)

        if surface_proche >= 0.02 :
            self.turn(90)
            
            
    
       

    





if __name__ == '__main__':

    MAX_SPEED = 6.28
    TIME_STEP = 64
    robot = SeatechRobot()

  
    
    while robot.step(TIME_STEP) != -1:
        
        
        robot.turn(8)
        robot.reperrage()
        robot.run_away()
        robot.radar_recul()
        pass


