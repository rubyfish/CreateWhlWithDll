from setuptools import setup, Distribution, find_packages
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setup(
    name="test_whl", #package name
    version="1.0.0",
    author="fish",
    description="test package whl with c++ dll",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'test_whl':[ # folder include dll
        'test_hello_world.dll'
        ],
    },
    python_requires='>=3.7',
)