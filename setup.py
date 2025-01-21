from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e . '

def get_requiremnts(file_path:str)->List[str]:
    requirents= []
    with open(file_path) as file:
        requirents = file.readlines()
        requirents = [req.replace('\n', '') for req in requirents]
    if HYPEN_E_DOT in requirents:
        requirents.remove(HYPEN_E_DOT)
    return requirents


setup(
    name= 'mlproject',
    version= '1.0.1',
    author='AkshataG',
    author_email='akshtag29@gmail.com',
    packages=find_packages(),
    install_package = get_requiremnts('requirements.txt')
    
)