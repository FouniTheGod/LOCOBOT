import math
from interbotix_xs_modules.locobot import InterbotixLocobotXS

# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true'

def setMenu(texte, choixMin, choixMax):
    """Génère un menu à partir d'un texte et d'un intervalle  de valeurs pour le choix"""
    
    while choix < choixMin || choixMax < choix:
        choix = int(input(MENU_ARTICULATION))
        
        if choix < choixMin || choixMax < choix:
            print("Le choix doit être compris entre " + str(choixMin) + " et " + str(choixMax))
            
    return choix


def toDegree(rad):
    """Convertie les radians en degrés"""
    return rad * 180 / math.pi


def main():
    MENU_ARTICULATION = "Choisissez une articulation:\n 1- Waist\n 2- Shoulder\n 3- Elbow\n 4- Wrist angle\n 5- Wrist rotate"
    MENU_ANGLE = "Unité d'angle:\n -1 Radian\n -2 Degré"
    
    articulations = ["waist", "shoulder", "elbow", "wrist_angle", "wrist_rotate"]
    
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200")
    
    joint = setMenu(MENU_ARTICULATION, 1, 5)
    unit = setMenu(MENU_ANGLE, 1, 2)
    
    angle = float(input("Angle (rad) ? "))
    
    if unit == 2:
        angle = toDegree(angle)
    
    # Set la position de base du bras
    locobot.arm.go_to_home_pose()
    # Applique la modification
    locobot.arm.set_single_joint_position(articulations[joint], angleRotation)
    
if __name__=='__main__':
    main()
