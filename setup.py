from setuptools import setup, find_packages

setup(
    name="systoptia",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["psutil", "GPUtil", "rich"],
    entry_points={
        "console_scripts": [
            "systoptia=systoptia.main"
        ]
    },
    author='Dhanush Kandhan',
    description='A CLI tool for Monitoring, Optimizing, and Refactoring Embedded and Computer Systems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dhanushk-offl/systoptia',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)