from setuptools import setup, find_packages

setup(
    name="test",
    packages=find_packages(include=["ab"]),
    python_requires=">=3.7.1",
    install_requires=[
    ],
    extras_require={
        "test": [
            "pytest",
        ]
    },
)

