from setuptools import setup, find_packages

setup(
    name="smolagents",              # Package name
    version="0.1",                  # Version
    packages=find_packages(where="src"),  # Find all packages
    package_dir={"": "src"},        # Tell setuptools where packages are
    install_requires=[              # Dependencies
        'requests>=2.25.1',
        'pandas>=1.2.0',
    ],
    author="Sheroze Ajmal",             # Optional metadata
    description="A sample package",
)