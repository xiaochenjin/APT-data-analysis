#https://cython.readthedocs.io/en/latest/src/quickstart/build.html
import distutils.core
import Cython.Build
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy


distutils.core.setup(
#	ext_modules = Cython.Build.cythonize("pure_SDM_2.pyx"),
	ext_modules = Cython.Build.cythonize("pure_rdf.pyx"),
	include_dirs=[numpy.get_include()])





