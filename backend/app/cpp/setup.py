from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "cpp_inference",
        ["inference.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-O3"],
    ),
]

setup(
    name="cpp_inference",
    ext_modules=ext_modules,
)
