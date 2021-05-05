from setuptools import setup, find_packages

setup(
    name ='ParamRunner',
    version ='1.0.0',
    author ='Yannick Bijl',
    author_email ='yannick.bijl@gmail.com',
    url ='https://github.com/yannickbijl/ParamRunner',
    description ='ParamRunner is a CLI tool for running the same command with different parameter settings.',
    long_description = open('README.md').read(),
    long_description_content_type ="text/markdown",
    license ='LICENSE',
    packages = find_packages(),
    entry_points ={
        'console_scripts': [
            'paramrunner = paramrunner.ParamRunner:main'
        ]
    },
    classifiers =(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
    )
)