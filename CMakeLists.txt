cmake_minimum_required(VERSION 3.20)

project(nice_auto_clicker VERSION 1.0
LANGUAGES C)

# libraries
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK4 REQUIRED IMPORTED_TARGET gtk4)

# for the IDE
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE src
"src/*.c"
)

include_directories(src)
add_executable(${PROJECT_NAME} ${src})

target_link_libraries(${PROJECT_NAME} PRIVATE PkgConfig::GTK4)
