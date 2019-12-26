
from automate_openfast.cmake import CMakeProject
from automate_openfast.git import Repo
from automate_openfast.rtest import OpenFASTRegTest

project_url = "https://github.com/rafmudaf/openfast"
git_branch = "dev"

# project_directory = "c:/Users/rmudafor/Desktop/openfast"  # Windows
# project_directory = "/home/rmudafor/Desktop/openfast"     # Eagle
project_directory = "/Users/rmudafor/Desktop/openfast"    # MBP

openfast_repo = Repo(project_url, project_directory)
openfast_repo.clone(branch=git_branch, force=True)

openfast_cmake = CMakeProject(project_directory, clean=True)
openfast_cmake.initialize(
    # cmake_generator="Visual Studio 15 2017 Win64",
    cmake_flags=[
        "-DBUILD_TESTING=ON",
        # "-DCTEST_OPENFAST_EXECUTABLE=C:/Users/rmudafor/Desktop/openfast_226/install/bin/beamdyn_driver.exe",
        # "-DCTEST_BEAMDYN_EXECUTABLE=C:/Users/rmudafor/Desktop/openfast_226/install/bin/openfast.exe"
    ],
)
openfast_cmake.build(cmake_build_type="Release", cmake_target="install")

rtest = OpenFASTRegTest(openfast_cmake)
rtest.machine = "macos"
rtest.compiler = "gnu"
rtest.tolerance = 1e-5
case_list = [
    "AWT_YFix_WSt",
    "AWT_WSt_StartUp_HighSpShutDown",
    "AWT_YFree_WSt",
    "AWT_YFree_WTurb",
    "AWT_WSt_StartUpShutDown",
    "AOC_WSt",
    "AOC_YFree_WTurb",
    "AOC_YFix_WSt",
    "UAE_Dnwind_YRamp_WSt",
    "UAE_Upwind_Rigid_WRamp_PwrCurve",
    "WP_VSP_WTurb_PitchFail",
    "WP_VSP_ECD",
    "WP_VSP_WTurb",
    "SWRT_YFree_VS_EDG01",
    "SWRT_YFree_VS_EDC01",
    "SWRT_YFree_VS_WTurb",
    "5MW_Land_DLL_WTurb",
    "5MW_OC3Mnpl_DLL_WTurb_WavesIrr",
    "5MW_OC3Trpd_DLL_WSt_WavesReg",
    "5MW_OC4Jckt_DLL_WTurb_WavesIrr_MGrowth",
    "5MW_ITIBarge_DLL_WTurb_WavesIrr",
    "5MW_TLP_DLL_WTurb_WavesIrr_WavesMulti",
    "5MW_OC3Spar_DLL_WTurb_WavesIrr",
    "5MW_OC4Semi_WSt_WavesWN",
    "5MW_Land_BD_DLL_WTurb",
    "WP_Stationary_Linear",
    "Ideal_Beam_Fixed_Free_Linear",
    "Ideal_Beam_Free_Free_Linear",
    "5MW_Land_BD_Linear"
]
rtest.execute_case_list(case_list)

rtest.update_baselines()
