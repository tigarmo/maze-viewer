import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "excludes": ["numpy.linalg", "numpy.core._dotblas", "numpy.linalg.lapack_lite"]
}

setup(  name = "maze-viewer",
        version = "0.1",
        description = "Simple Maze Viewer",
        options = {"build_exe": build_exe_options},
        executables = [Executable("maze-viewer.py", base=None)])