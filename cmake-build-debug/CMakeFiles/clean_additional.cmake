# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\PoCQet_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\PoCQet_autogen.dir\\ParseCache.txt"
  "PoCQet_autogen"
  )
endif()
