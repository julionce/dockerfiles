###############################################################################
# Crosstool-NG
###############################################################################

FROM ubuntu

RUN apt update \
&&  apt install -y \
        git \
        automake \
        build-essential \
        flex \
        bison \
        texinfo \
        unzip \
        help2man \
        file \
        gawk \
        libtool-bin \
        libncurses5-dev \
        wget \
        rsync \
        python-dev \
&&  rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/crosstool-ng/crosstool-ng.git && cd crosstool-ng \
&&  ./bootstrap &&  ./configure &&  make &&  make install \
&&  cd .. && rm -rf crosstool-ng