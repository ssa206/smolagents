from setuptools import setup, find_packages

setup(
    name="smolagents",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={
        "smolagents": ["prompts/*.yaml"],
    },
    install_requires=[              # Dependencies
        'requests>=2.25.1',
        'pandas>=1.2.0',
    ],
    author="Sheroze Ajmal",             # Optional metadata
    description="A sample package",
)