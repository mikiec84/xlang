cmake_minimum_required(VERSION 3.9)

add_subdirectory(cpp)
add_subdirectory(idl)
add_subdirectory(python)

if (WIN32)
    add_subdirectory(natvis)
endif()