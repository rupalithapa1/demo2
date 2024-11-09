from setuptools import find_packages,setup
from typing import List

HYPHEN_E_NOT ='-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements =[]
    with open("requirements.txt") as file_obj:
        requirements =file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_NOT in requirements:
            requirements.remove(HYPHEN_E_NOT)

    return requirements

setup(
    name="new_project",
    author="rupali thapa",
    author_email="roopthapa143@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)

