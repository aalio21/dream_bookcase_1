from setuptools import setup, find_packages

setup(
    name="dream_bookcase",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "networkx",
        "pyvis"
    ],
    author="Your Name",
    description="Visual tools for the Dream Bookcase of reason vs. irrationality",
    python_requires=">=3.7"
)
