###############################################################################
# VSCODE devcontainer dockerfile
###############################################################################
ARG BASE_IMAGE=ubuntu

FROM $BASE_IMAGE

ARG USERNAME=urosu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
&&  useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
&&  apt update \
&&  apt install -y sudo \
&&  echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
&&  chmod 0440 /etc/sudoers.d/$USERNAME \
&&  rm -rf /var/lib/apt/list/*

USER $USERNAME