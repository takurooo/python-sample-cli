from setuptools import find_packages, setup

with open("requirements.txt") as f:
    install_requirements = f.read().splitlines()

setup(
    name="samplecli",
    version="0.0.1",
    description="sample cli",
    author="takurooo",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "samplecli=samplecli.main:hello",
        ]
    },
)
