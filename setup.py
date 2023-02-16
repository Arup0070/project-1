from setuptools import setup
from typing import List
Requierments_file_name = "requirements.txt"
def get_requirements_list()->List[str]:
    """Description: this function going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mention"""
    with open(Requierments_file_name) as requirement_file:
        return requirement_file.readlines()
    

Project_name= "housing-predictor"
Version="0.0.1"
Author="Arup"
Description="This the 1st FSDS Project"
Packages=["housing"]
setup(
    name=Project_name,
    version=Version,
    author=Author,
    description=Description,
    packages= Packages,
    install_requires = get_requirements_list()

)

