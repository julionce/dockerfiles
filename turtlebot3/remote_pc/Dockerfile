###################################################################################################
# TurtleBot3 in Ubuntu 18.04
###################################################################################################
FROM osrf/ros2:nightly

# Install Cartographer dependencies.
RUN apt update
RUN apt install -y \
        google-mock \
        libceres-dev \
        liblua5.3-dev \
        libboost-dev \
        libboost-iostreams-dev \
        libprotobuf-dev \
        protobuf-compiler \
        libcairo2-dev \
        libpcl-dev \
        python3-sphinx

# Install Gazebo9.
RUN curl -sSL http://get.gazebosim.org | sh

# Install Navigation2 dependencies.
RUN apt install -y \
        libsdl-image1.2 \
        libsdl-image1.2-dev \
        libsdl1.2debian \
        libsdl1.2-dev

# Install TurtleBot3.
RUN mkdir -p ~/turtlebot3_ws/src
RUN bash -c \ 
    "cd ~/turtlebot3_ws && \
    source \"/opt/ros/$ROS_DISTRO/setup.bash\" && \
    wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/ros2/turtlebot3.repos && \
    vcs import src < turtlebot3.repos && \
    colcon build --symlink-install"
RUN echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc

# Install time sync dependencies
RUN apt install -y ntpdate

# Set TurtleBot model
ENV TURTLEBOT3_MODEL=waffle_pi
