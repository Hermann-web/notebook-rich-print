from setuptools import setup, find_packages

setup(
    name='notebook-rich-print',
    version='1.0.0',
    author='Your Name',
    author_email='agossouhermann7@gmail.com',
    description='A Python module for rich-text printing in notebooks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hermann-web/notebook-rich-print',
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
