import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

import random


class TurtleSpawner(Node):

    def __init__(self):
        super().__init__('turtle_spawner')
        self.spawn_client = self.create_client(Spawn, 'spawn')
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.spawn_turtle()

    def spawn_turtle(self):
        request = Spawn.Request()
        request.name = 'turtle2'
        request.x = random.uniform(0.5, 10.5)
        request.y = random.uniform(0.5, 10.5)
        request.theta = random.uniform(0, 2 * 3.14159265)
        self.spawn_client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    spawner = TurtleSpawner()
    rclpy.spin_once(spawner)
    spawner.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()