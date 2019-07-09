# Qt Creator Dockerfile

This dockerfile install Qt Creator from the official install script using a non-interactive [controller script](https://doc.qt.io/qtinstallerframework/noninteractive.html).
Use the following command to run a Docker container with desktop output:

```bash
xhost +
sudo docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix
```
