from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="opencv-compare",
    version="0.0.2",
    author="sjjeong94",
    author_email="sjjeong94@gmail.com",
    packages=["opencv_compare"],
    license="MIT",
    description="A simple image comparison tool, in OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjjeong94/opencv-compare",
    install_requires=["opencv-python"],
)
