# tp_turtle_regulation_Angelo_Clemence
Dans la partie 1 de notre Tp nous avons cree un ROS complet pour contrôler une tortue dans Turtlesim le nom du package est turtle_regulationavec les dépendances nécessaires (rospy, std_msgs, turtlesim), suivi de l'implémentation du nœud set_way_point.py qui souscrit au topic /turtle1/pose pour récupérer la position de la tortue, calcule l'angle et la distance vers le waypoint cible via des formules trigonométriques. composantes clés  sont: 
1.	régulation de cap, 
2.	régulation de distance, 
3.	service dynamique. 
Le nœud set_way_point.py s'abonne au topic /turtle1/pose pour obtenir la position actuelle, calcule l'angle et la distance vers un way_point fixe (5.0, 5.0) en utilisant des formules trigonométriques (math.atan2 pour l'angle, distance euclidienne pour la position), puis publie des commandes de vitesse (Twist) sur /turtle1/cmd_vel avec une régulation proportionnelle (Kp) pour ajuster la vitesse linéaire et angulaire. Tourne vers le point !" → Elle ajuste sa direction.

Un seuil de tolérance (0.1 unités) arrête la tortue à proximité du waypoint, tandis qu'un topic /is_moving signale si le mouvement est actif. "Avance doucement !" → Plus elle est loin, plus elle va vite.


 Le système inclut également la création d'un service personnalisé (Set_Way_Point.srv) dans un package dédié (turtle_interfaces), permettant de modifier dynamiquement le waypoint via un appel de service. Elle s’arrête quand elle est presque arrivée.Et si on change le point magique, elle recommence !

