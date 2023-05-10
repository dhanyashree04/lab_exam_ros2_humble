    #!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.turtle1_pose = None
        self.turtle2_pose = None

        # PID gains
        self.kp = 0.0999
        self.ki = 0.0009
        self.kd = 0.0099

        self.error = 0.0
        self.integral = 0.0
        self.derivative = 0.0
        self.previous_error = 0.0

        self.publisher_ = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.subscriber1_ = self.create_subscription(Pose, 'turtle1/pose', self.turtle1_pose_callback, 10)
        self.subscriber2_ = self.create_subscription(Pose, 'turtle2/pose', self.turtle2_pose_callback, 10)

    def turtle1_pose_callback(self, msg):
        self.turtle2_pose = msg

        if self.turtle1_pose is not None:
            self.update()

    def turtle2_pose_callback(self, msg):
        self.turtle1_pose = msg

        if self.turtle2_pose is not None:
            self.update()

    def update(self):
        # calculate the error between the two turtles
        error_x = self.turtle1_pose.x - self.turtle2_pose.x
        error_y = self.turtle1_pose.y - self.turtle2_pose.y
        self.error = math.sqrt(error_x*2 + error_y*2)

        # calculate the PID terms
        self.integral += self.error
        self.derivative = self.error - self.previous_error
        self.previous_error = self.error

        # calculate the velocity command
        cmd_vel = Twist()
        cmd_vel.linear.x = self.kp*self.error + self.ki*self.integral + self.kd*self.derivative
        cmd_vel.angular.z = 2.0*math.atan2(error_y, error_x)

        # publish the velocity command
        self.publisher_.publish(cmd_vel)

        # check if the turtle has reached the goal
        if self.error < 0.1:
            self.kill_turtle1()

    def kill_turtle1(self):
        # stop the turtle1
        cmd_vel = Twist()
        self.publisher_.publish(cmd_vel)

        # kill the turtle1
        self.destroy_node()
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)

    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()