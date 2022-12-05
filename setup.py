from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(['fib_c_annoted.pyx'],
                                annotate=True, language_level=3))
