cmake_minimum_required(VERSION 3.20)

project(nice_auto_clicker VERSION 1.0
LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(FLTK_BUILD_SHARED_LIBS OFF)

# libraries
add_subdirectory(dependencies/fltk)

# for the IDE
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE src
"src/*.cpp"
)

include_directories(src)
add_executable(${PROJECT_NAME} ${src})

target_link_libraries(${PROJECT_NAME} PRIVATE fltk)
