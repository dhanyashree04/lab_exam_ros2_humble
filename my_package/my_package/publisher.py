#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from std_msgs.msg import String



class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.get_logger().info("Publisher node started")
        self.publisher_= self.create_publisher(String,"/message",10) #to create the topic to publish a string 
        # self.counter_= 0
        self.timer_=self.create_timer(1.0,self.publish_message)
    def publish_message(self):
        msg = String()
        msg.data =  "Hello " #+ str(self.counter_) typecasting converting string to
        self.publisher_.publish(msg)
        #self.counter_+=1
    
def main(args=None):
    rclpy.init(args=args)
    node=Publisher()
    rclpy.spin(node)
    rclpy.shutdown()    


if __name__ == "__main__":
    main()