cmake_minimum_required(VERSION 3.5)
project(turtle_regulation)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(PROGRAMS
  turtle_regulation/set_way_point.py
  DESTINATION lib/${PROJECT_NAME}
)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "turtle_regulation/set_way_interface.srv"
)

ament_package()