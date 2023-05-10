
cmake_minimum_required(VERSION 3.25)

# Set the C++ stanadard globally
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(pybind11_template)

find_package(pybind11 CONFIG REQUIRED)
find_package(my_lib CONFIG REQUIRED)


pybind11_add_module(my_lib MODULE my_lib_wrapper.cpp)
target_link_libraries(my_lib PRIVATE my_lib::my_lib)
target_compile_definitions(my_lib PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS my_lib DESTINATION my_lib)

