import math
from interbotix_xs_modules.locobot import InterbotixLocobotXS

# This script 
#
# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true'
# Then change to this directory and type 'python move_base.py'

def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200", use_move_base_action=True)
    
    locobot.arm.go_to_home_pose()
    locobot.arm.set_single_joint_position("elbow", 3*math.pi/2.0)
    
    locobot.base.move(0.6, -0.1, 4)
    
    locobot.arm.set_ee_pose_components(x=0.3, y=-0.2, z=1, roll=0, pitch=0.5)
    locobot.gripper.close()
    
    locobot.arm.set_single_joint_position("waist", math.pi/2.0)
    
    locobot.arm.go_to_home_pose()
    locobot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()
