
import os
import shutil
import subprocess


class Repo():
    def __init__(self, url, local_directory):
        self.url = url
        self.local_directory = local_directory
    
    def clone(self, branch="master", force=False):
        if os.path.isdir(self.local_directory) and not force:
            raise FileExistsError
        elif os.path.isdir(self.local_directory) and force:
            shutil.rmtree(self.local_directory, ignore_errors=force)

        subprocess.run(
            [
                "git",
                "clone",
                "--recursive",
                "-b",
                "{}".format(branch),
                "{}".format(self.url),
                "{}".format(self.local_directory)
            ],
            check=True
        )
        self.current_branch = branch
