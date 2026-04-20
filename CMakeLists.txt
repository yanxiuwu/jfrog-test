cmake_minimum_required(VERSION 3.20)
project(conan_demo)

find_package(fmt REQUIRED)
find_package(spdlog REQUIRED)

add_executable(demo main.cpp)
target_link_libraries(demo fmt::fmt spdlog::spdlog)
