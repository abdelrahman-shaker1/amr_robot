from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_share = get_package_share_directory('amr_description')

    world = os.path.join(pkg_share, 'worlds', 'my_worlds.sdf')
    robot = os.path.join(pkg_share, 'urdf', 'amr_robot.sdf')

    # Launch Gazebo Fortress
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={'gz_args': world}.items()
    )

    # Spawn robot
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'amr_robot', '-file', robot],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])
