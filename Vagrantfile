# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/id_rsa.pub"
  config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa"
  config.vm.provision "shell", inline: <<-SHELL
    cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys
  SHELL
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/focal64"
 # config.ssh.username = 'prince'
  #config.ssh.password = 'drones'
  #config.ssh.insert_key = false
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./ros_ws", "/home/vagrant/ros_ws"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = true
    vb.name = "foxy_box"
    # Customize the amount of memory on the VM:
    vb.memory = "4096"

    vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y ubuntu-desktop
    sudo apt-get install virtualbox-guest-dkms virtualbox-guest-utils virtualbox-guest-x11

    echo "Installing ROS 2 Foxy Fitzroy \n\n"

    echo "Setting up Locale \n"
    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    echo "Setting up Sources \n"
    sudo apt update && sudo apt install curl gnupg2 lsb-release
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

    echo "Installing ROS 2 packages \n"
    echo "export CHOOSE_ROS_DISTRO=foxy" >> ~/.bashrc
    source ~/.bashrc
    sudo apt-get update
    sudo apt-get install -y ros-$CHOOSE_ROS_DISTRO-desktop
    sudo apt-get install -y ros-$CHOOSE_ROS_DISTRO-ros-base

    echo "Installing optional argcomplete \n"
    sudo apt install -y python3-pip
    pip3 install -U argcomplete

    export CHOOSE_ROS_DISTRO=foxy
    source /opt/ros/$CHOOSE_ROS_DISTRO/setup.bash
    echo "source /opt/ros/$CHOOSE_ROS_DISTRO/setup.bash" >> ~/.bashrc

    ####ROS2 swarm installation: https://github.com/ROS2swarm/ROS2swarm/blob/master/INSTALL_GUIDE.md
    sudo apt-get update
    # Install colcon, Gazebo, Navigation2
    sudo apt -y  install python3-colcon-common-extensions
    sudo apt -y install ros-foxy-gazebo-ros-pkgs ros-foxy-cartographer  ros-foxy-cartographer-ros
    sudo apt -y install ros-foxy-navigation2 ros-foxy-nav2-bringup
    # sudo apt-get install -y ros-$CHOOSE_ROS_DISTRO-rmw-opensplice-cpp # for OpenSplice
    # sudo apt-get install -y ros-$CHOOSE_ROS_DISTRO-rmw-connext-cpp # for RTI Connext (requires license agreement)
    ########################################################################################
    #######################Install turtlebot3##############################################
    mkdir -p ~/turtlebot3_ws/src
    cd ~/turtlebot3_ws/src/
    git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
    git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
    sudo apt install ros-foxy-dynamixel-sdk -y
    cd ~/turtlebot3_ws && colcon build --symlink-install
    echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
    echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
    ####Switch to supported commits
    cd ~/turtlebot3_ws/src/
    git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
    cd  ~/turtlebot3_ws/src/turtlebot3
    git checkout 8237b796ea1571033bf3230fbc78d1143968ddd1
    cd ~/turtlebot3_ws/src/turtlebot3_msgs
    git checkout cf5c56be94b335b1d2c9817bd2dcaceec21ccc68
    echo 'export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models' >> ~/.bashrc
    cd ~/turtlebot3_ws && colcon build --symlink-install
    echo 'export TURTLEBOT3_MODEL=waffle_pi' >> ~/.bashrc
    source ~/.bashrc
    ########################################################################################
    cd
    git clone https://github.com/ROS2swarm/ROS2swarm.git
    cd ~/ROS2swarm
    colcon build --symlink-install
    echo 'source ~/ROS2swarm/install/setup.bash' >> ~/.bashrc
    source ~/.bashrc
  SHELL
end
