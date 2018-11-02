#########################################################################################
# A Dockerfile for the micro-ROS simulation environment
#########################################################################################
FROM ubuntu:16.04
WORKDIR /root

#########################################################################################
# Install NuttX dependencies
#########################################################################################
RUN apt-get update 
RUN apt-get install -y \
            build-essential \ 
            bison \
            flex \
            gperf \
            libgmp-dev \
            libmpc-dev \
            libmpfr-dev \
            libisl-dev \
            binutils-dev \
            libelf-dev \
            libexpat-dev \
            libz-dev \
            libncurses-dev \
            gettext \
            texinfo \
            wget \
            gcc-arm-none-eabi \ 
            gdb-arm-none-eabi

#########################################################################################
# Install utils
#########################################################################################
RUN apt-get install -y \
            git \
            cmake \
            remake \
            vim \
            openocd \
            screen \
            libusb-1.0.0-dev 

#########################################################################################
# Build kconfig-frontends
#########################################################################################
RUN git clone https://bitbucket.org/nuttx/tools     
RUN cd tools/kconfig-frontends && \
    ./configure --enable-mconf --disable-nconf --disable-gconf --disable-qconf && \
    LD_RUN_PATH=/usr/local/lib && \
    make && \
    make install && \
    ldconfig 

