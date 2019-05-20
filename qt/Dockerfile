###################################################################################################
# Qt Creator dockerfile
###################################################################################################
FROM ubuntu:latest
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