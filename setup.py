import pathlib
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setuptools.setup(
    name="r3x-python-sdk",
    version="0.0.2",
    description="RubiX Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rubixFunctions/r3x-python-sdk",
    author="RubiX Function",
    author_email="r3xfunctions@gmail.com",
    license="Apache-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
    ],
    packages=["r3x"],
    include_package_data=True,
    install_requires=[],
)