#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class Sample(Node):
    #constructor will run everytime we create the object
    def __init__(self): #self is rclpy library for the node
        #inheritence of parent node --super command 
        super().__init__('sample')
        print('hi')
        #self.get_logger().info("ROS2") #similar to print statement self is the rclpy created node
        self.get_logger().info("Node Started")
        self.timer_ = self.create_timer(1.0,self.timer_callback) #
    def  timer_callback(self):
        self.get_logger(  ).info("ROS 2")   
            



def main(args=None):          #colon is used for every function
    rclpy.init(args=args) #initialisation
    node=Sample()
    rclpy.spin(node)   #talking-listening hello thing  asking to spin the node created
    rclpy.shutdown()   #stops the communication

if __name__ == "__main__":     
    main()