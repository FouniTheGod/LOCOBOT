import math
from interbotix_xs_modules.locobot import InterbotixLocobotXS

# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true'

def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200")
    
    pressure = float(input("Pressure (de 0 jusqu'à 3.68 exclu) ? "))
    
    locobot.gripper.open()
    locobot.gripper.set_pressure(pressure)
    
    locobot.gripper.close()
    
if __name__=='__main__':
    main()
