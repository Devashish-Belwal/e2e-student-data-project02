from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of packages.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace('\n', '') for req in requirements if req.strip() and not req.startswith('#')]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name='e2e-student-data-project02',
version='0.0.1',
author='Devashish',
author_email='433devashish@gmail.com',
description='End to End Student Data Project',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)