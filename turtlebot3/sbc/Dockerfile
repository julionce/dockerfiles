###################################################################################################
# SBC in Ubuntu 18.04
###################################################################################################
FROM ubuntu:18.04 

# Install dependencies
RUN apt update
RUN apt install -y \
        build-essential \
        cmake \
        git \
        wget

# Clone Micro XRCE-DDS repository.
RUN git clone --recursive https://github.com/eProsima/Micro-XRCE-DDS.git ~/uxrce

# Install Agent.
RUN cd ~/uxrce/agent && \
    git checkout a495c65faa964ddc068ac6e1249f17f5c9f92787 && \
    mkdir build && cd build && \
    cmake -DTHIRDPARTY=ON -DCONFIG_UDP_TRANSPORT_MTU=8192 -DCONFIG_SERIAL_TRANSPORT_MTU=8192 .. && \
    make install && \
    mkdir ~/turtlebot3 && \
    cp ../DEFAULT_FASTRTPS_PROFILES.xml ~/turtlebot3 && \
    ldconfig /usr/local/lib

# Install time sync dependencies
RUN apt install -y ntpdate

# Download firmware
RUN cd ~/turtlebot3 && \
    wget https://github.com/ROBOTIS-GIT/OpenCR_Binaries/raw/master/turtlebot3/ROS2/latest/opencr_update.tar.bz2 && \
    tar -xf ./opencr_update.tar.bz2

ENV OPENCR_PORT=/dev/ttyACM0
ENV OPENCR_MODEL=waffle
