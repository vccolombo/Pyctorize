from setuptools import setup

setup(
    name="pyctorize",
    version="1.0",
    description="A Python CLI program to extract frames of videos",
    url="https://github.com/vccolombo/pyctorize",
    author="Víctor Cora Colombo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "click==7.0",
        "moviepy==1.0.0"
    ],
    entry_points={
        "console_scripts": ["pyctorize=pyctorize.pyctorize:pyctorize"],
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
