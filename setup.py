# setup.py
from setuptools import setup, find_packages

setup(
    name="systoptia",
    version="0.1.0",
    packages=find_packages(include=['*']),
    install_requires=[
        'click>=8.0.0',
        'psutil>=5.8.0',
        'GPUtil>=1.4.0',
        'rich>=10.0.0'
    ],
    entry_points={
        "console_scripts": [
            "systoptia=.cli.commands:run_cli"  # Point directly to your main.py's main function
        ],
    },
    author="Dhanush K",
    description="A comprehensive system optimization and monitoring tool",
    python_requires=">=3.6",
)