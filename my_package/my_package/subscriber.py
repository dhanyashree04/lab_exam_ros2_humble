#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import String


class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.counter=0
        self.publisher_ = self.create_publisher(String,"/count",10)
        self.get_logger().info("Node started by subscriber...")
        self.subscriber_ = self.create_subscription(String,'/message',self.msg_callback,10)
        
    def msg_callback(self, msg):
        msg_a = String()
        self.get_logger().info(msg.data)
        msg_a.data = str(self.counter)
        self.publisher_.publish(msg_a)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)          #initialsing the argument first step after creating main program
    node=Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":                # declaring the main program
    main()