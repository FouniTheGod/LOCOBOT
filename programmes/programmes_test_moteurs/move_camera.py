from interbotix_xs_modules.locobot import InterbotixLocobotXS
from math import pi

# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200'

def to_degree(deg):
    return deg * pi / 180

def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200") #use_move_base_action=True)
    
    joint_name = str(input("Joint name ? [pan, tilt] "))
    angle = float(input("Angle (rad) ? "))
    
    locobot.camera.pan_tilt_go_home()
    
    if (joint_name == "pan"):
        locobot.camera.pan(angle)
        
    elif (joint_name == "tilt"):
        locobot.camera.tilt(angle)

if __name__=='__main__':
    main()
