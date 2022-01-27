import math
import time
from interbotix_xs_modules.locobot import InterbotixLocobotXS

# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true'

def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200")
    
    diff_time = 1
    
    joint_name = str(input("Joint name ? "))
    angle = float(input("start angle (rad) ? "))
    increment = float(input("step size (±) ? "))
    
    #locobot.arm.set_single_joint_position("waist", 0.0)
    locobot.arm.go_to_home_pose()
    
    #locobot.arm.set_single_joint_position("elbow", 1.0)
    locobot.arm.set_single_joint_position(joint_name, angle)
    
    while diff_time > 0.1:
    
        print(round(angle, 3), "(", round(diff_time,3), "s)")
        angle += increment
        
        diff_time = time.time()
        locobot.arm.set_single_joint_position(joint_name, angle)
        diff_time = time.time() - diff_time
    
if __name__=='__main__':
    main()
