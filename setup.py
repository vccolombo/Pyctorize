from setuptools import setup

setup(
    name="pyctorize",
    version="0.1",
    author="Víctor Cora Colombo",
    author_email="victorcora98@gmail.com",
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
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
