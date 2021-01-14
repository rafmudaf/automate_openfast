
import os
import subprocess
import shutil


class CMakeProject():
    def __init__(self, project_directory, build_directory="build", clean=False):
        self.project_directory = project_directory
        self.build_directory = os.path.join(project_directory, build_directory)

        if clean or not os.path.isdir(self.build_directory):
            shutil.rmtree(self.build_directory, ignore_errors=True)
            os.makedirs(self.build_directory)

    def initialize(
        self,
        cmake_generator=None,
        cmake_architecture=None,
        cmake_flags=None):
        """
        Run the initial CMake call which generates CMakeCache.txt and
        other initial files for the build system.

        cmake_generator (Str): The generator type; typically one of

            - Unix Makefiles
            - Visual Studio 14 2015
            - Visual Studio 15 2017
            - NMake Makefiles
            - Xcode
        
        architecture (Str): The architecture type for the build; typically
            left empty to use the default for the system. For Visual Studio
            generators, this would by one of

                - "Win32" for 32 bit
                - "x64" for 64 bit
        
        cmake_flags [Str]: Additional flags for configuring CMake; the syntax is
            ["-DCMAKEFLAG=ON", "-DANOTHERFLAG=OFF"]
        """
        os.chdir(self.build_directory)
        command = ["cmake", self.project_directory]
        self.cmake_generator = cmake_generator
        if cmake_generator:
            command += ["-G" + cmake_generator]
        if cmake_architecture:
            command += ["-A" + cmake_architecture]
        if cmake_flags:
            command += cmake_flags
        subprocess.run(command, check=True)

    def build(
        self,
        cmake_target=None,
        cmake_build_type="Release"):
        """
        target (Str): One of the build targets included in the CMake project;
            typically one of

            - "openfast" on any platform
            - "all" on any platform
            - "install" on any platform
            - "ALL_BUILD" with Visual Studio
            - "test" on any platform to run the full test suite
        
        cmake_build_type (Str): One of

            - Release
            - RelWithDebInfo
            - MinSizeRel
            - Debug
        """
        os.chdir(self.build_directory)
        command = [
            "cmake",
            "--build",
            "."
        ]

        # Apply the build config target for Visual Studio generators
        if "visual" in self.cmake_generator.lower():
            command += ["--config", cmake_build_type]

        if cmake_target:
            command += ["--target", cmake_target]
        subprocess.run(command, check=True)
