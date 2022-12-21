from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    talkerNode = Node(
        package='drone_publish',
        executable='DroneTalker',
        name='DroneTalker',
    )
    publishNode = Node(
            package='drone_publish',
            executable='DataFusionListener',
            name='DataFusionListener'
        )
    clientNode = Node(
        package='drone_publish',
        executable='DroneClient',
        name='DroneClient'
    )
    launch = LaunchDescription([clientNode, publishNode, talkerNode])
    return launch
