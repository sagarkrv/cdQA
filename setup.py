import os
from setuptools import setup, find_packages


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="cdqa",
    version="1.3.10",
    author="Pragnesh Krishnan",
    description="An End-To-End Closed Domain Question Answering System",
    keywords="reading comprehension question answering deep learning natural language processing information retrieval bert",
    license="Apache-2.0",
    url="https://github.com/cdqa-suite/cdQA",
    packages=find_packages(),
    install_requires=read("requirements_cdqa.txt").split(),
)
