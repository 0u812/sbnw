cmake_minimum_required (VERSION 2.8)
project (SagittariusSandbox)

if(SBNW_SPYDER_DIST)
  install(FILES widgets/externalshell/sitecustomize.py DESTINATION python2/spyderlib/widgets/externalshell)
endif()
