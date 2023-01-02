from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="image-compare",
    version="0.0.1",
    author="sjjeong94",
    author_email="sjjeong94@gmail.com",
    packages=["image_compare"],
    license="MIT",
    description="A simple image comparison tool, in OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjjeong94/image-compare",
    install_requires=["opencv-python"],
)
