
from automate_openfast.cmake import CMakeProject
from automate_openfast.git import Repo
import os
import shutil

###
# Run this with the 32 bit Intel VS cmd
###

project_url = "https://github.com/openfast/openfast"
git_branch = "v2.5.0"
project_directory = "c:/Users/rmudafor/Desktop/openfast_25"

# Clone the repository
openfast_repo = Repo(project_url, project_directory)
# openfast_repo.clone(branch=git_branch, shallow=True)

# Compile and package all binaries
## Create the packaged directory
packaged_directory = os.path.join(project_directory, git_branch)
if os.path.isdir(packaged_directory):
    shutil.rmtree(packaged_directory, ignore_errors=True)
os.makedirs(packaged_directory)

## 32 bit single precision
single_32bit = CMakeProject(project_directory, build_directory="build_32single")
single_32bit.initialize(
    cmake_generator="NMake Makefiles",
    cmake_flags=["-DDOUBLE_PRECISION=OFF", "-DCMAKE_BUILD_TYPE=RELEASE"],
)
single_32bit.build(cmake_target="openfast")
shutil.copyfile(
    os.path.join(single_32bit.build_directory, "glue-codes", "openfast", "openfast.exe"),
    os.path.join(packaged_directory, "openfast_Win32.exe")
)
