﻿# CMakeList.txt : CMake project for AoC++, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("AoC++")

# Add source to this project's executable.
add_executable (AoC++ "AoC++.cpp" "AoC++.h"  "aocDay01.h" "aocDayXX.h" "aocDay02.h")

# TODO: Add tests and install targets if needed.
