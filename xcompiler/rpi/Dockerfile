###############################################################################
# cross-compier/rpi
###############################################################################
FROM ubuntu

ARG RPI_VERSION=rpi2-3_raspbian_buster_gcc-8.3.0

RUN apt update \
&&  apt install -y \
        wget \
        python \
        qemu \
&&  rm -rf /var/lib/apt/list/*

COPY url.py /root

RUN wget -O xcompiler.tar.gz $(python /root/url.py $RPI_VERSION) \
&&  mkdir xcompiler \
&&  tar xf xcompiler.tar.gz -C xcompiler --strip-components 1 \
&&  rm xcompiler.tar.gz \
&&  mv xcompiler /opt \
&&  echo 'export PATH=/opt/xcompiler/bin:$PATH' >> ~/.bashrc \
&&  echo 'export LD_LIBRARY_PATH=/opt/xcompiler/lib:$LD_LIBRARY_PATH' >> ~/.bashrc

RUN rm /root/url.py
COPY toolchain.cmake /opt/xcompiler