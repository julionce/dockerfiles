#########################################################################################
# A Dockerfile for Raspberry Pi 
#########################################################################################
FROM ubuntu:18.04
WORKDIR /root

RUN apt update

# Install utils.
RUN apt install -y \
        vim \
        ranger

# Install Raspberry Pi dependencies.
RUN apt install -y \
        build-essential \
        cmake \
        git \
        bison \
        flex \
        libssl-dev \
        bc

# Install Raspberry Pi toolchain.
RUN git clone --depth=1 git://github.com/raspberrypi/tools.git
ENV PATH=/root/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin:$PATH

# Get Raspberry Pi sources.
RUN git clone --depth=1 https://github.com/raspberrypi/linux
#RUN cd linux && \
#    KERNEL=kernel7 && \
#    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig && \
#    make -j4 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- all \
