
from automate_openfast.cmake import CMakeProject
from automate_openfast.git import Repo
import os
import shutil

project_url = "https://github.com/openfast/openfast"
git_branch = "v2.2.0"
project_directory = "c:/Users/rmudafor/Desktop/openfast_v2"

# Clone the repository
openfast_repo = Repo(project_url, project_directory)
openfast_repo.clone(branch=git_branch)

# Compile and package all binaries
## Create the packaged directory
packaged_directory = os.path.join(project_directory, git_branch)
if os.path.isdir(packaged_directory):
    shutil.rmtree(packaged_directory, ignore_errors=True)
os.makedirs(packaged_directory)

## 64 bit double precision
double_64bit = CMakeProject(project_directory, build_directory="build_64double")
double_64bit.initialize(
    cmake_generator="Visual Studio 15 2017 Win64",
    cmake_flags=["-DDOUBLE_PRECISION=ON"],
)
double_64bit.build(cmake_build_type="Release", cmake_target="ALL_BUILD")
shutil.copyfile(
    os.path.join(double_64bit.build_directory, "glue-codes", "openfast", "Release", "openfast.exe"),
    os.path.join(packaged_directory, "openfast_x64_double.exe")
)

## 64 bit single precision
single_64bit = CMakeProject(project_directory, build_directory="build_64single")
single_64bit.initialize(
    cmake_generator="Visual Studio 15 2017 Win64",
    cmake_flags=["-DDOUBLE_PRECISION=OFF"],
)
single_64bit.build(cmake_build_type="Release", cmake_target="ALL_BUILD")
shutil.copyfile(
    os.path.join(single_64bit.build_directory, "glue-codes", "openfast", "Release", "openfast.exe"),
    os.path.join(packaged_directory, "openfast_x64.exe")
)

## 32 bit single precision
single_32bit = CMakeProject(project_directory, build_directory="build_32single")
single_32bit.initialize(
    cmake_generator="Visual Studio 15 2017",
    cmake_flags=[
        "-DDOUBLE_PRECISION=OFF",
        "-DCMAKE_Fortran_COMPILER=C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2019.5.281/windows/bin/intel64/ifort.exe",
        "-DCMAKE_C_COMPILER=C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2018/windows/bin/intel64/icl.exe",
        "-DCMAKE_CXX_COMPILER=C:/Program Files (x86)/IntelSWTools/compilers_and_libraries_2018/windows/bin/intel64/icl.exe"
    ],
)
single_32bit.build(cmake_build_type="Release", cmake_target="ALL_BUILD")
shutil.copyfile(
    os.path.join(single_32bit.build_directory, "glue-codes", "openfast", "Release", "openfast.exe"),
    os.path.join(packaged_directory, "openfast_Win32.exe")
)

