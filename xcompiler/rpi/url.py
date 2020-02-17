#!/usr/bin/python

import sys

url_map = {
    "rpi2-3_raspbian_buster_gcc-8.3.0": "https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Buster/GCC%208.3.0/Raspberry%20Pi%202%2C%203/cross-gcc-8.3.0-pi_2-3.tar.gz/download",
    "rpi2-3_raspbian_buster_gcc-9.2.0": "https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Buster/GCC%208.3.0/Raspberry%20Pi%202%2C%203/cross-gcc-8.3.0-pi_2-3.tar.gz/download",
    "rpi64_raspbian_stretch_gcc-6.3.0": "https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Stretch/GCC%206.3.0/Raspberry%20Pi%203A%2B%2C%203B%2B%2C%204/cross-gcc-6.3.0-pi_3%2B.tar.gz/download",
    "rpi64_raspbian_stretch_gcc-9.2.0": "https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Stretch/GCC%209.2.0/Raspberry%20Pi%203A%2B%2C%203B%2B%2C%204/cross-gcc-9.2.0-pi_3%2B.tar.gz/download",
    "rpi64_raspbian_buster_gcc-8.3.0": "https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Buster/GCC%208.3.0/Raspberry%20Pi%203A%2B%2C%203B%2B%2C%204/cross-gcc-8.3.0-pi_3%2B.tar.gz/download",
    "rpi64_raspbian_buster_gcc-9.2.0": "https://sourceforge.net/projects/raspberry-pi-cross-compilers/files/Raspberry%20Pi%20GCC%20Cross-Compiler%20Toolchains/Buster/GCC%209.2.0/Raspberry%20Pi%203A%2B%2C%203B%2B%2C%204/cross-gcc-9.2.0-pi_3%2B.tar.gz/download",
}

rpi_version = sys.argv[1]

if rpi_version in url_map:
    print(url_map[sys.argv[1]])
