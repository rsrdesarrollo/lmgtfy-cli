from setuptools import setup

VERSION='1.0.1'

setup(
    author='Raul Sampedro',
    author_email='rsrdesarrollo@gmail.com',
    name='lmgtfy',
    version=VERSION,
    packages=['lmgtfy'],
    url='https://github.com/rsrdesarrollo/lmgtfy-cli/tarball/{}'.format(VERSION),
    license='GPLv3',
    description='Let me Google that for you CLI link generator.',
    scripts=['src/lmgtfy'],
    keywords=['cli', 'google', 'search', 'generator'],
    requires=['clipboard']
)
