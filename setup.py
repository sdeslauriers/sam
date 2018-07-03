from setuptools import setup

setup(
    name='sam',
    version='0.0.0',
    packages=['sam'],
    url='https://github.com/sdeslauriers/sam',
    license='MIT',
    author='Samuel Deslauriers-Gauthier',
    author_email='sam.deslauriers@gmail.com',
    description='A Python package that contains Sam\'s python tools.',
    install_requires=['numpy', 'streamlines', 'nibabel', 'vtk', 'nimesh',
                      'scikit-image']
)
