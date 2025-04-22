#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

import math

class SetWayPoint(Node):
    def __init__(self):
        super().__init__('set_way_point')
        
        # Configuration initiale
        self.waypoint = [7.0, 7.0]  # Partie 1
        self.distance_tolerance = 0.1  # Partie 2
        self.Kp = 2.0  # Gain rotation (Partie 1)
        self.Kpl = 1.0  # Gain distance (Partie 2)
        
        # Etat de la tortue
        self.turtle_pose = None
        self.is_moving = False
        
        # Publishers/Subscribers
        self.pose_sub = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.moving_pub = self.create_publisher(Bool, 'is_moving', 10)  # Partie 2

    def pose_callback(self, msg):
        self.turtle_pose = msg
        dx = self.waypoint[0] - self.turtle_pose.x
        dy = self.waypoint[1] - self.turtle_pose.y
        
        # Calcul distance (Partie 2)
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < self.distance_tolerance:
            cmd_msg = Twist()  # Stop
            self.is_moving = False
        else:
            self.is_moving = True
            
            # Commande rotation (Partie 1)
            theta_desired = math.atan2(dy, dx)
            error_angle = math.atan(math.tan((theta_desired - self.turtle_pose.theta)/2))
            u = self.Kp * error_angle
            
            # Commande linéaire (Partie 2)
            v = min(self.Kpl * distance, 2.0)  # Limite la vitesse
            
            cmd_msg = Twist()
            cmd_msg.linear.x = v
            cmd_msg.angular.z = u
        
        # Publications
        self.cmd_vel_pub.publish(cmd_msg)
        self.moving_pub.publish(Bool(data=self.is_moving))  # Partie 2

def main(args=None):
    rclpy.init(args=args)
    node = SetWayPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()