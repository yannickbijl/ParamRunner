__author__ = "Yannick Bijl"
__copyright__ = "Copyright 2021, Yannick Bijl"
__email__ = "yannick.bijl@gmail.com"
__license__ = "MIT"

import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    print("Please install setuptools before installing paramrunner.", file=sys.stderr)
    exit(1)

setup(
    name="paramrunner",
    version="0.0.1",
    author="Yannick Bijl",
    author_email="yannick.bijl@gmail.com",
    description="paramrunner is a CLI tool for running the same command with different parameter settings.",
    license="MIT",
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    package_data={"": ["*.sh"]},
    entry_points={'console_scripts': ['paramrunner = paramrunner.paramrunner:main']},
    install_requires=["pyyaml"],
    classifiers =(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
    )
)
