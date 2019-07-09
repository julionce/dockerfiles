FROM ubuntu:18.04
WORKDIR /root

RUN apt update

# Install dependencies.
RUN apt install -y \
        build-essential \
        gawk \
        git \
        texinfo \
        flex \
        bison \
        file \
        wget

# Download sources.
RUN git clone -b 'binutils-2_28' --depth 1 git://sourceware.org/git/binutils-gdb.git binutils
RUN git clone -b 'glibc-2.24' --depth 1 git://sourceware.org/git/glibc.git
RUN git clone -b 'gcc-6_3_0-release' --depth 1 git://gcc.gnu.org/git/gcc.git gcc-6.3.0
RUN git clone -b 'gcc-9_1_0-release' --depth 1 git://gcc.gnu.org/git/gcc.git gcc-9.1.0
RUN git clone --depth 1 https://github.com/raspberrypi/linux

# Download prerequisites.
RUN cd gcc-6.3.0 && contrib/download_prerequisites
RUN cd gcc-9.1.0 && contrib/download_prerequisites

RUN mkdir -p /opt/cross-pi-gcc

# Copy RPi's headers.
ENV KERNEL=kernel7
RUN cd linux && make ARCH=arm INSTALL_HDR_PATH=/opt/cross-pi-gcc/arm-linux-gnueabihf headers_install

# Build binutils.
RUN mkdir binutils/build && \
    cd binutils/build && \
    ../configure --prefix=/opt/cross-pi-gcc --target=arm-linux-gnueabihf --with-arch=armv6 --with-fpu=vfp --with-float-hard --disable-multilib && \
    make -j8 && \
    make install

# Build gcc and glibc.
RUN mkdir gcc-6.3.0/build && \
    cd gcc-6.3.0/build && \
    ../configure --prefix=/opt/cross-pi-gcc --target=arm-linux-gnueabihf --enable-languages=c,c++,fortran --with-arch=armv6 --with-fpu=vfp --with-float=hard --disable-multilib && \
    make -j8 && \
    make install



