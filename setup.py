'''
setup.py file for the ml_project package.
This file is used to specify the package metadata and dependencies.
Alao it is used to install project as a package using pip command so it will be easy for others to use it.

'''


from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> list[str]:
    #This function will return the list of requirements (as in list of packages to be installed)
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="Abhisar Dhengare",
    author_email="abhisardhengare@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description="A machine learning project setup",
)