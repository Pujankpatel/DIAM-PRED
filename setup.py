from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


# apde get_requirement nu function banvya chhe je list hase string na form ma
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in
                        requirements]  # Hava jyare 1line joina comlete thai pachi \n ava ana read nathi karavanu etla ena "" replace kairu

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='DiamondPricePredic',
    version='0.0.1',
    author='Pujan',
    author_email='pujanpatel80@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)