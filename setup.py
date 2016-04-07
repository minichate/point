import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "celestron-point",
    version = "0.0.1",
    author = "Christopher Troup",
    author_email = "minichate@gmail.com",
    description = ('Control Celestron telescopes from Python'),
    license = "BSD",
    keywords = "celestron, nextstar, telescope",
    url = "https://github.com/minichate/point",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
