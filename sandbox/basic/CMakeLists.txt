cmake_minimum_required (VERSION 2.8)
project (SagittariusSandbox)

add_executable(basic basic.c)
target_link_libraries(basic sbnw)
set_target_properties( basic PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=1 )

add_executable(issue_46 issue_46.c)
target_link_libraries(issue_46 sbnw)
set_target_properties( issue_46 PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=1 )

add_executable(issue_48 issue_48.c)
target_link_libraries(issue_48 sbnw)
set_target_properties( issue_48 PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=1 )

add_executable(cubic-test cubic-test.cpp)
target_link_libraries(cubic-test sbnw)
set_target_properties( cubic-test PROPERTIES COMPILE_DEFINITIONS SBNW_CLIENT_BUILD=1 )

# Install
install(TARGETS basic issue_46 issue_48 cubic-test DESTINATION bin)
install(FILES mpl-cubic.py DESTINATION bin)
