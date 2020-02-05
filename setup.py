from setuptools import setup, find_packages

setup(
    name="dt_wrapper",
    version="1.2.2",
    author="Vincent Turnier",
    email="vincentturnier@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
)