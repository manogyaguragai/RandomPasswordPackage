from setuptools import setup, find_packages

setup(
    name='random-password-generator-pckg', 
    version='0.1',  
    description='A simple customizable random password generator package.',  
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    author='Manogya Guragai',
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