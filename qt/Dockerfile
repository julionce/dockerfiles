###################################################################################################
# Qt Creator dockerfile
###################################################################################################

# Download Qt installer from official website.
RUN wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run
RUN chmod +x ./qt-unified-linux-x64-online.run

# Copy and run Qt script in order to avoid interactive installation.
COPY qt-noninteractive.qs /root/qt-noninteractive.qs
RUN ./qt-unified-linux-x64-online.run --script qt-noninteractive.qs -platform minimal
