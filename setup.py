import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numerical-algorithms-pgrzy",
    version="0.0.1",
    author="Patryk Grzybala",
    author_email="pat.grzybala@gmail.com",
    description="Project with problems from Numerical Algorithms classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nevrast/numercial_algorithms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
