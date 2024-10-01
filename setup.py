from setuptools import setup, find_packages

setup(
    name='RandomPasswordGenPKG', 
    version='0.1',  
    description='A simple customizable random password generator package.',  
    long_description=open('README.md').read(), 
    long_description_content_type='markdown', 
    author='Manogya',
    author_email='manogyaguragai24@gmail.com',
    url='https://github.com/manogyaguragai', 
    packages=find_packages(),  
    classifiers=[ 
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)