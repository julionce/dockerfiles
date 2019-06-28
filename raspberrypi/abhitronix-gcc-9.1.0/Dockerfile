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
        bc \
        wget

# Install Raspberry Pi toolchain.
RUN wget 'https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/GCC%209.1.0/Raspberry%20Pi%202%2C%203/cross-gcc-9.1.0-pi_2-3.tar.gz'
RUN tar xf cross-pi-gcc-9.1.0-pi_2.3.tar.gz
RUN rm cross-pi-gcc-9.1.0-pi_2.3.tar.gz
RUN mv cross-pi-gcc-9.1.0-1 /opt
RUN echo 'export PATH=/opt/cross-pi-gcc-9.1.0-1/bin:$PATH' >> .profile
RUN echo 'export LD_LIBRARY_PATH=/opt/cross-pi-gcc-9.1.0-1/lib:$LD_LIBRARY_PATH' >> .profile
