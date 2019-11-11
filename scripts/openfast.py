
from automate_openfast.cmake import CMakeProject
from automate_openfast.git import Repo
from automate_openfast.rtest import OpenFASTRegTest

openfast_repo = Repo("https://github.com/rafmudaf/openfast", "/Users/rmudafor/Desktop/openfast_raf")
# openfast_repo.clone(branch="dev")

openfast_cmake = CMakeProject("/Users/rmudafor/Desktop/openfast_raf")
openfast_cmake.initialize()
openfast_cmake.build(cmake_build_type="Debug", cmake_target="beamdyn_driver")

rtest = OpenFASTRegTest(openfast_cmake)
rtest.machine = "macos"
rtest.compiler = "gnu"
rtest.tolerance = 1e-5
case_list = [
    "AWT_YFix_WSt",
    "AWT_WSt_StartUp_HighSpShutDown",
    "AWT_YFree_WSt",
    "AWT_YFree_WTurb"
]
rtest.execute_case_list(case_list)
