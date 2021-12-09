Documentation LoCoBot
# **Présentation**
LoCoBot est avant tout un robot qui comprend un système de manipulation, ainsi qu’une base mobile sur laquelle il est monté. Ce robot est conçu pour faire tourner PyRobot, une interface légère de haut niveau et open source au-dessus du système d’exploitation (ROS). Cette interface tourne sur système Unix, plus  exactement sur la distribution Ubuntu. L’utilisation de la version 20.04 est préconisée, et c’est également celle que nous utilisons.

Le robot est constitué des composantes suivantes, à savoir :

- Une base mobile : Yujin Robot Kobuki Base (YMR-K01-W1)
- Un bras robotique articulé : WidowX 200 Mobile Manipulator
- Un ordinateur embarqué : Intel NUC NUC7i5BNH Mini PC
  - Processeur Intel Core i3 8109U de 8ème génération : 2 cœurs cadencés entre 2,2 et 3,4GHz
  - 8 Go de mémoire RAM
  - 250 Go de stockage sur SSD
  - Partie graphique intégrée Intel Iris Plus Graphics
  - Compatible WiFi / Bluetooth 4.0
- Une caméra : Intel® RealSense™ Depth Camera D435
- Des servomoteurs Dynamixel
- Une central IMU 3 axes avec gyroscope, accéléromètre, magnétomètre et détecteur de collisions et d’arêtes

Détails techniques :

- Vitesse maximale de déplacement : 70 cm/s
- Vitesse maximale angulaire : 180 deg/s
- Charge maximale : 2 kg
- Autonomie en fonctionnement : 4 à 6h (dépendant du chargement)
- Temps de charge : 2 à 3h

- Nom du robot : locobot
- Modèle du robot : locobot\_wx200
# **Lancement du LoCoBot**
## **Matériel à prévoir**
Avant toute chose, il est important de se prémunir du matériel nécessaire pour manipuler le robot en plus de ce qui est fourni. Est à prévoir :

- Un clavier et une souris
- Un écran avec un câble HDMI / câble VGA + adaptateur HDMI vers VGA
- Un ordinateur avec un système d’exploitation Unix installé
- Une clé USB bootable avec distribution Ubuntu 20.04 (pour le premier démarrage seulement)

Du matériel non nécessaire peut toutefois être apprécié pour certains usages ou recommandés, à savoir :

- Un hub USB pour combler le nombre limité de ports USB
- Un câble Ethernet pour connecter le robot au réseau local en filaire à l’instar du WiFi
## **Allumer le robot**
Tout d’abord, il s’agit d’allumer le robot. Pour cela, il faut :

1. Allumer la base en appuyant sur le bouton ON/OFF présent au niveau de la base Kobuki. Ainsi une lumière verte s’allume, accompagné d’un signal sonore. Si la lumière est jaune, c’est que la base doit être rechargée
1. Allumer la batterie en appuyant sur le bouton d’alimentation circulaire de celle-ci, située juste en dessous de l’ordinateur embarqué (NUC). Ainsi, un indicateur lumineux où jusqu’à 4 LEDs s’allument, correspondant à la capacité de la batterie. S’il n’y a qu’une seule LED d’allumée, c’est que la batterie doit être chargée
1. Allumer l’ordinateur embarqué en appuyant sur le bouton d’alimentation. Si tout s’est passé correctement le voyant va devenir bleu

Ensuite, si ce n’est pas déjà fait, connectez la souris, le clavier et l’écran au robot. Si c’est le premier allumage, branchez la clé USB bootable et suivez les instructions pour installer Ubuntu 20.04 sur le LoCoBot. Si une distribution est déjà installée, choisissez l’option pour effacer la version précédente et installer la nouvelle. 
# **Installation**
(détailler le processus d’installation du LoCoBot)
