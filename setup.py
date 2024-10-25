# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="project",
    ext_modules=cythonize("gsm_logger.pyx"),
)
