cmake_minimum_required (VERSION 2.8)
project (SagittariusSandbox)

if(GRAPHFAB_SPYDER_DIST)
  install(FILES p_pyfab.py DESTINATION python2/spyderplugins)
endif()
