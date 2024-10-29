from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'random', 'unittest'
    ],
    author='Paula Limmer',
    author_email='paula.limmer@fau.de',
    description='A math quiz application',
    url='https://github.com/PaulaLim/dsss_homework_2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
