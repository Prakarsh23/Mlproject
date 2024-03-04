##Automatically finds all packages in ML application directory that we have created
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='_e .'

def get_requirements(file_path:str)->List[str]:
    ## This function will return will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        ##readlines give \ when reading the next line so we are replacing it with blank
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

## meta data info about the entire project
setup(
name = 'mlproject',
version = '0.0.1' ,
author = 'Prakarsh' ,
author_email= 'prakarsh.tewari@gmail.com' ,
## Checks in how many folders do we have the __init__.py file and consider those folders as packages & try to build it
packages=find_packages() ,
##install_requires = ['pandas','numpy','seaborn']
install_requires = get_requirements('requirement.txt')
)