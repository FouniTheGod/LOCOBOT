from interbotix_xs_modules.locobot import InterbotixLocobotXS
from math import pi

# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200'

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
    MENU_ARTICULATION = "Choisissez une articulation:\n 1- Pan\n 2- Tilt"
    MENU_ANGLE = "Unité d'angle:\n -1 Radian\n -2 Degré"
    
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200")
    
    joint = setMenu(MENU_ARTICULATION, 1, 2)
    unit = setMenu(MENU_ANGLE, 1, 2)
    
    angle = float(input("Angle ? "))
    
    if unit == 2:
        angle = toDegree(angle)
    
    # Remise de la caméra à sa position de base
    locobot.camera.pan_tilt_go_home()
    
    if (joint_name == "pan"):
        locobot.camera.pan(angle)
        
    elif (joint_name == "tilt"):
        locobot.camera.tilt(angle)

if __name__=='__main__':
    main()
