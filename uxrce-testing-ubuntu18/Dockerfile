#########################################################################################
# Micro XRCE-DDS testing docker
#########################################################################################

FROM ubuntu:18.04
WORKDIR home/

# Essentials
RUN apt-get update
RUN apt-get install -y \
            software-properties-common \
            build-essential \
            cmake \
            git \
            vim \
            ranger

# Java
RUN apt install -y openjdk-8-jdk

# Gradle
RUN apt-get install -y gradle
RUN apt-get clean
