import os
import subprocess
import shutil
from multiprocessing import Process, Queue, current_process
import queue
import time

class OpenFASTRegTest():
    def __init__(self, project, binary_name="openfast"):
        self.project = project
        self.binary_name = binary_name

        # Copy the test-case turbine files to the build directory
        for d in ["5MW_Baseline", "AOC", "AWT27", "SWRT", "UAE_VI", "WP_Baseline"]:
            data_directory = os.path.join(self.project.build_directory, d)
            if not os.path.isdir(data_directory):
                shutil.copytree(
                    os.path.join(self.project.project_directory, "reg_tests", "r-test", "glue-codes", "openfast", d),
                    data_directory
                )

    def execute_case(self, case_name):
        os.chdir(os.path.join(self.project.project_directory, "reg_tests"))

        command = [
            "python",
            "manualRegressionTest.py",
            os.path.join("..", "install", "bin", self.binary_name),
            self.machine,
            self.compiler,
            self.tolerance,
            "-case", case_name
        ]
        subprocess.run(command, check=True)        

    def execute_queue(self, remaining, finished):
        """
        remaining: (Queue) - The Queue of cases that still need to run
        finished: (Queue) - The Queue of finished cases
        """
        while True:
            try:
                # try to get task from the queue. get_nowait() function will 
                # raise queue.Empty exception if the queue is empty. 
                # queue(False) function would do the same task also.
                case_name = remaining.get_nowait()
            except queue.Empty:
                break
            else:
                # if no exception has been raised, add the task completion 
                # message to finished queue
                self.execute_case(case_name)
                finished.put(case_name + ' is done by ' + current_process().name)

    def execute_case_list(self, case_list):
        number_of_processes = 4

        # Build the Queue of cases to run and to store finished cases
        remaining_queue = Queue()
        for case in case_list:
            remaining_queue.put(case)
        finished = Queue()

        # Launch the processes for the queue
        processes = []
        for _ in range(number_of_processes):
            p = Process(
                target=self.execute_queue,
                args=(remaining_queue, finished)
            )
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        while not finished.empty():
            print(finished.get())

    def update_baselines(self):
        os.chdir(os.path.join(self.project.project_directory, "reg_tests", "r-test"))
        command = [
            "python",
            "updateBaselineSolutions.py",
            os.path.join("glue-codes", "openfast", "CaseList.md"),
            os.path.join(self.project.build_directory, "reg_tests", "glue-codes", "openfast"),
            os.path.join("glue-codes", "openfast"),
            self.machine,
            self.compiler
        ]
        subprocess.run(command, check=True)

    @property
    def machine(self):
        return self._machine

    @machine.setter
    def machine(self, value):
        valid_values = [
            "linux",
            "macos",
            "windows"
        ]
        if value.lower() not in valid_values:
            raise ValueError
        self._machine = value

    @property
    def compiler(self):
        return self._compiler

    @compiler.setter
    def compiler(self, value):
        valid_values = [
            "gnu",
            "intel"
        ]
        if value.lower() not in valid_values:
            raise ValueError
        self._compiler = value

    @property
    def tolerance(self):
        return str(self._tolerance)

    @tolerance.setter
    def tolerance(self, value):
        self._tolerance = value
