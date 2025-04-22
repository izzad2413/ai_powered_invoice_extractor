from setuptools import find_packages, setup  # Import the necessary functions from setuptools for packaging and distributing Python projects.
from typing import List  # Import List from typing to specify that we will be working with lists of strings in this script.

HYPEN_E_DOT = '-e .'  # Define a constant variable that represents a common entry in requirements.txt to refer to the current project.

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a file and returns a list of requirements.
    It removes any instances of '-e .' from the list.
    '''
    requirements = []  # Initialize an empty list to store the requirements.

    with open(file_path) as file_obj:  # Open the file at the given file_path.
        requirements = file_obj.readlines()  # Read all lines in the file and store them in the requirements list.
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters from each requirement.

        if HYPEN_E_DOT in requirements:  # Check if '-e .' is in the list of requirements.
            requirements.remove(HYPEN_E_DOT)  # If present, remove it from the list.

    return requirements  # Return the cleaned list of requirements.

setup(
    name='mlproject',  # Name of your project.
    version='0.0.1',  # Version of your project.
    author='Izzad',  # Author's name.
    author_email='nazmirulizzadnassir@gmail.com',  # Author's email address.
    packages=find_packages(),  # Automatically find and include all packages in the project.
    install_requires=get_requirements('requirements.txt')  # Specify the dependencies for the project by reading the requirements.txt file.
)
