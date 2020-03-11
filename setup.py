import setuptools

with open("README.md", "r") as fileHelper:
    long_description = fileHelper.read()

setuptools.setup(
    name="merge-pkg-AnSchwarzkopf", 
    version="0.0.1",
    author="Andreas Schwarzkopf",
    author_email="schwarzkopf.and@gmail.com",
    description="A package to merge intervals and output overlapping intervals.",
    long_description=long_description,
    url="https://github.com/AnSchwarzkopf/MergeIntervals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)