cmake_minimum_required (VERSION 2.8)
project (Graphfab)

install(FILES AntimonyPowerLaw.xml DESTINATION testcases)
install(FILES BorisEJB.xml DESTINATION testcases)
install(FILES ConservedCycles.xml DESTINATION testcases)
install(FILES EquilibRaw.xml DESTINATION testcases)
install(FILES GlycolysisOriginal.xml DESTINATION testcases)
install(FILES testbigmodel.xml DESTINATION testcases)
# install(FILES internal/bounding_box.xml
#   internal/EquilibRaw_wlayout-DrawNetwork-vs2010.xml internal/example2.xml
#   internal/twocompsys-ex.xml DESTINATION testcases/internal)