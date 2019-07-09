###################################################################################################
# Qt Creator dockerfile
###################################################################################################
ARG BASE_IMAGE=ubuntu:latest
FROM $BASE_IMAGE
WORKDIR /root

RUN apt update
RUN apt install -y \
        libdbus-1-3 \
        libfreetype6 \
        libfontconfig1 \
        libx11-dev \
        libx11-xcb-dev \
        wget

# Download Qt installer from official website.
RUN wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run
RUN chmod +x ./qt-unified-linux-x64-online.run

# Copy and run Qt script in order to avoid interactive installation.
COPY qt-noninteractive.qs /root/qt-noninteractive.qs
RUN ./qt-unified-linux-x64-online.run --script qt-noninteractive.qs -platform minimal

# Remove unnecessary files.
RUN rm qt-noninteractive.qs qt-unified-linux-x64-online.run
