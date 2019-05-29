import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyafs",
    version="1.0.1",
    author="afs",
    author_email="author@example.com",
    description="Lo que el cuerpo necesita",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bcrypt', 'passlib', 'unidecode', 'libxml2-dev', 'libxslt-dev', 'python-dev', 'lxml',
    ],                 
)