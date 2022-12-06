# nxp_hovergames


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

You should be able to see the messages sent between the nodes
