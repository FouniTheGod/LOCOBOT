from interbotix_xs_modules.locobot import InterbotixLocobotXS
def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200", use_move_base_action=True)
    locobot.base.move_to_pose(10, 245, 0, True)

if __name__=='__main__':
    main()
    
