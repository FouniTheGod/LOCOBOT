from interbotix_xs_modules.locobot import InterbotixLocobotXS

# To get started, open a terminal and type...
# 'roslaunch interbotix_xslocobot_control xslocobot_python.launch robot_model:=locobot_wx200 use_nav:=true localization:=true'
# Then change to this directory and type 'python move_base.py'

def setMenu(texte, choixMin, choixMax):
    """Génère un menu à partir d'un texte et d'un intervalle  de valeurs pour le choix"""
    
    while choix < choixMin || choixMax < choix:
        choix = int(input(MENU_ARTICULATION))
        
        if choix < choixMin || choixMax < choix:
            print("Le choix doit être compris entre " + str(choixMin) + " et " + str(choixMax))
            
    return choix


def toDegreePerSecond(radPerSecond):
    """Convertie les rad/s en deg/s"""
    return radPerSecond * 180 / math.pi


def main():
    MENU_ANGLE = "Unité de vitesse angulaire:\n -1 Rad/s\n -2 Deg/s"
    
    locobot = InterbotixLocobotXS(robot_model="locobot_wx200", arm_model="mobile_wx200", use_move_base_action=True)

    translation = float(input("Vitesse (en m/s) ? "))
    unit = setMenu(MENU_ANGLE, 1, 2)
    rotation = float(input("Vitesse de rotation ? "))
    time = float(input("Temps d'exécution (en s) ? "))
    
    if unit == 2:
        rotation = toDegreePerSecond(angle)
    
    # Effectue le déplacement
    locobot.base.move(translation, rotation, time)

if __name__=='__main__':
    main()
