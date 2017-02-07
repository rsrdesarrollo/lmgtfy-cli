from setuptools import setup

setup(
    author='Raul Sampedro',
    author_email='rsrdesarrollo@gmail.com',
    name='lmgtfy',
    version='1.0.1',
    packages=['lmgtfy'],
    url='https://github.com/rsrdesarrollo/lmgtfy-cli',
    license='GPLv3',
    description='Let me Google that for you CLI link generator.',
    scripts=['src/lmgtfy'],
    keywords=['cli', 'google', 'search', 'generator'],
    requires=['clipboard']
)
