cmake_minimum_required(VERSION 3.8)
project(ec_single_axis_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ethercat_driver REQUIRED)
find_package(ethercat_interface REQUIRED)
#find_package(ethercat_plugins REQUIRED)

install(
  DIRECTORY config ros2_control
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
