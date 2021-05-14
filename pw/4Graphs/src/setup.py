from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        r'matriceadjacence',
        [r'matriceadjacence.py']
    ),
]

setup(
    name='matriceadjacence',
    ext_modules=cythonize(ext_modules),
)
