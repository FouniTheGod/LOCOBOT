import math
from interbotix_xs_modules.locobot import InterbotixLocobotXS

# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true'

def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200")
    
    joint_name = str(input("Joint name ? [waist, shoulder, elbow, wrist_angle, wrist_rotate] "))
    angle = float(input("Angle (rad) ? "))
    
    #locobot.arm.set_single_joint_position("waist", 0.0)
    locobot.arm.go_to_home_pose()
    
    #locobot.arm.set_single_joint_position("elbow", 1.0)
    locobot.arm.set_single_joint_position(joint_name, angle)
    
if __name__=='__main__':
    main()
