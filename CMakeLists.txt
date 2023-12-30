cmake_minimum_required(VERSION 3.6)
project(sab LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 14)

set(SABIN ${PROJECT_SOURCE_DIR}/bin)
include(cmake/color.cmake)

find_package(PkgConfig REQUIRED)
pkg_search_module(HTS REQUIRED IMPORTED_TARGET "htslib")

find_package(Threads REQUIRED)

find_package(Intellia)
if (${Intellia_FOUND}) 
    message(STATUS "${Green}Found Intellia C++ Lib on the system level${ColourReset}")
    set(USE_INTELLIA_NAMESPACE TRUE)
else()
    message(STATUS "${Yellow}Failed to find Intellia C++ Lib, use subdirectory${ColourReset}")
    set(USE_INTELLIA_NAMESPACE FALSE)
    add_subdirectory(CppLib)
endif()

add_subdirectory(src)

if (CMAKE_BUILD_TYPE MATCHES Release)

    # Intellia Python Lib
    find_program(HAS_INTELLIA_PYTHONLIB "gff2fa")
    if (NOT HAS_INTELLIA_PYTHONLIB)
        message(STATUS "${Yellow}CMaking Intellia Python Lib ${ColourReset}")
        include(cmake/intellia_pythonlib.cmake)
    endif ()

endif()
