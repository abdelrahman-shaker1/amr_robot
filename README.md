Autonomous Mobile Robot (AMR) - ROS 2 Simulation

This repository contains the simulation files for an Autonomous Mobile Robot (AMR) using ROS 2 Humble and Gazebo Fortress.
Features

    Robot Model: Differential drive system with a 2D LIDAR sensor.

    Environment: Custom Gazebo world with integrated physics and gravity.

    Communication: ROS 2 bridge for LIDAR data and velocity commands.

Project Structure

    src/amr_description/urdf/: Contains the .sdf and .xacro robot models.

    src/amr_description/launch/: Python scripts to launch the simulation.

    src/amr_description/worlds/: World files defining the simulation environment.
    
How to Run

    Source the Workspace:
    source install/setup.bash

    Set Graphics Platform:
    export QT_QPA_PLATFORM=xcb

    Launch:
    ros2 launch amr_description spawn_robot.launch.py
