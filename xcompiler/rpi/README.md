# RPi crosscompiler template

## How to build it?

```
docker build . --build-arg RPI_VERSION=<rpi-version> -t <image-name>
```

| OS        | Version       | RPi Model | GCC                           | `rpi-version`                         |
|-----------|---------------|-----------|-------------------------------|---------------------------------------|
| Raspbian  | Buster        | 2/3       | 8.3.0                         | **rpi2-3_raspbian_buster_gcc-8.3.0**  |
| Raspbian  | Buster        | 2/3       | 9.2.0<sup>[1](#fn1)</sup>     | **rpi2-3_raspbian_buster_gcc-9.2.0**  |
| Raspbian  | Stretch       | 3A+/3B+/4 | 6.3.0                         | **rpi64_raspbian_stretch_gcc-6.3.0**  |
| Raspbian  | Stretch       | 3A+/3B+/4 | 9.2.0<sup>[1](#fn1)</sup>     | **rpi64_raspbian_stretch_gcc-9.2.0**  |
| Raspbian  | Buster        | 3A+/3B+/4 | 8.3.0                         | **rpi64_raspbian_buster_gcc-8.3.0**   |
| Raspbian  | Buster        | 3A+/3B+/4 | 9.2.0<sup>[1](#fn1)</sup>     | **rpi64_raspbian_buster_gcc-9.2.0**   |

# How to use it?

It provides a CMake toolchain at */opt/xcompiler/toolchain.cmake* which contains all you need for cross-compiling a CMake project:

```
cmake .. -DCMAKE_TOOLCHAIN_FILE=/opt/xcompiler/toolchain.cmake && make
```

<a name="fn1">[1]</a>: Not provided by default. It must be installed separately.