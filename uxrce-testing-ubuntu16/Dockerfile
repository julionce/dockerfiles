#########################################################################################
# Micro XRCE-DDS testing docker
#########################################################################################

FROM ubuntu:16.04
WORKDIR home/

# Essentials
RUN apt-get update
RUN apt-get install -y \
            software-properties-common \
            build-essential \
            cmake \
            git \
            vim

# Java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections 
RUN add-apt-repository ppa:webupd8team/java 
RUN apt-get update 
RUN apt-get install -y oracle-java8-installer
RUN rm -rf /var/cache/oracle-jdk8-installer

# Gradle
RUN apt-get install -y gradle
RUN apt-get clean
