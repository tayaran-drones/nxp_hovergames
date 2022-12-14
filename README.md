# NXP HoverGames


## 1 - Up and Running with Vagrant
Download and install Vagrant.
Then to create the virtual machine, go to the source directory and run `vagrant up`

## 2 - Configure Python environment on your local machine (Optional)
You can develop code and work on your local machine while running on the virtual machine.
To do this, you can use the shared workspace directory (ros_ws). You can either ssh into
the virtual machine to run the code or add the python interpreter. 
---Steps for that can be found at this link:https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-virtual-boxes.html

## 3 - Compiling the environment on your machine
Go to ~/ros_ws and run `colcon build --symlink-install` to set up the ros package and 
compile the nodes.

## 4 - Installing and running the nodes
Open 2 new terminal and run `source ~/ros_ws/install/setup.bash` to add the created nodes.
In on of the terminals, run `ros2 run drone_publish DroneTalker`
In the other terminal, run `ros2 run  drone_publish DataFusionListener`

# Additional instructions

## Running Gazebo simulation

Open one terminal in the virtual machine and run 
`gazebo --verbose /opt/ros/foxy/share/gazebo_plugins/worlds/gazebo_ros_diff_drive_demo.world`
This will open a gazebo window with a moving block.
Then `vagrant ssh` to the virtual machine from your computer and run
`ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{linear: {x: 1.0}}' -1`
You should see the block start to move. More information can be found at: 
http://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros#TestingGazeboandROS2integration

## Running PX4 simulation

Go to PX4 directory `cd Firmware` and run `make px4_sitl jmavsim` or `make px4_sitl gazebo`
It will take some time, but the simulation should start and you will be able to command the quad copter.
Additional instructions can be found at: https://docs.px4.io/main/en/simulation/

You should be able to see the messages sent between the nodes
