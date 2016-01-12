from setuptools import setup, find_packages

with open('requirements.txt', 'r') as req:
    INSTALL_REQUIRES = [x.strip() for x in req.readlines()]

with open('README.rst', 'r') as desc:
    DESCRIPTION = desc.read()

setup(
    name='uempowering',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Som-Energia/uempowering',
    license='MIT',
    install_requires=INSTALL_REQUIRES,
    author='Som Energia, SCCL',
    author_email='info@somenergia.coop',
    description=DESCRIPTION
)
