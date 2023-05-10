#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import String
import time 
import math
 
class three_node(Node):
    def __init__(self):
        super().__init__("Three_node")
        self.get_logger().info("Node has been started.")
        self.counter = 0
        self.subscribe_=self.create_subscription(String, "/count",self.subscriber_callback,10)
        
    def subscriber_callback(self,msg_a):
         self.get_logger().info(msg_a.data)
         
def main(args=None):
    rclpy.init(args=args)
    node = three_node()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ =="main_":
    main()