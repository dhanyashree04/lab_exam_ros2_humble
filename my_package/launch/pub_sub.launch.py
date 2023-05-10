


def generate_launch_description():

    # Define the path to the package containing the nodes
    package_path = os.path.join(('/home/dhanyashree/ros2_ws/src/my_package/my_package/publisher.py'),('/home/dhanyashree/ros2_ws/src/my_package/my_package/subscriber.py'),('my_package'), 'launch')

    # Declare the publisher node
    publisher_node = launch_ros.actions.Node(
        package='my_package',
        executable='publisher',
        name='publisher'
    )

    # Declare the subscriber node
    subscriber_node = launch_ros.actions.Node(
        package='my_package',
        executable='subscriber',
        name='subscriber'
    )

    # Group the nodes together
    nodes = [publisher_node, subscriber_node]

    # Create the launch description with the list of nodes
    ld = launch.LaunchDescription(nodes)

    return ld