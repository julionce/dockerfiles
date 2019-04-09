# TurtleBot3 Dockerfiles

## Remote PC

* **How to build and run the Remote PC docker?**

On a terminal, run the following command:

```bash
# build 
$ sudo docker build ./remote_pc/ -t turtlebot3_remote_pc

# run
$ sudo docker run --rm -it turtlebot3_remote_pc
```

* **How to run the turtlebot3?**

Once inside the docker, run the follwing command:

```bash
$ ros2 launch turtlebot3_bringup robot.launch.py
```

## SBC

* **How to build and run the SBC?**

On a terminal, run the following command:

```bash
# build
$ sudo docker build ./sbc/ -t turtlebot3_sbc

# launch
$ sudo docker run --rm -it -v /dev/ttyACM0:/dev/ttyACM0 --net=host --privileged turtlebot3_sbc
```
* **How to flash the firmware into OpenCR?**

Once inside the docker, run the following command:

```bash
$ cd ~/turtlebot3/opencr_update
$ ./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr
```

* **How to run the Micro XRCE-DDS Agent for OpenCR?**

Once inside the docker, run the following command:

```bash
$ cd ~/turtlebot3 && MicroXRCEAgent serial /dev/ttyACM0
```
