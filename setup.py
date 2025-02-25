from setuptools import setup, find_packages
def get_requirements(filename):
    with open(filename) as f:
        requirements = [
            line.strip() for line in f
            if not line.startswith('#')
        ]
    return requirements

setup( name='RAG System',
    version='0.1',
    packages=find_packages(),
    author='Sushil Kumar',
    author_email='kmrsushil10@gamil.com',
    requires= get_requirements('requirements.txt')
)