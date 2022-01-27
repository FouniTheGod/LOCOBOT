from interbotix_xs_modules.locobot import InterbotixLocobotXS

# This script commands the base to move to an arbitrary point on a map
# Note that this script assumes you already have a map built
#
# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true localization:=true'
# Then change to this directory and type 'python move_base.py'

def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200", use_move_base_action=True)

    translation = float(input("Vitesse (en m/s) ? "))
    rotation = float(input("Vitesse de rotation (en rad/s) ? "))
    time = float(input("Temps d'exécution (en s) ? "))

    locobot.base.move(translation, rotation, time)

if __name__=='__main__':
    main()
