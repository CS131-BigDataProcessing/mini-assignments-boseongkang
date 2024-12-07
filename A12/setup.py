from setuptools import setup, find_packages

setup(
    name='crime_test',
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    author="Boseong Kang",
    description="A package which includes  statistic and validation function for crime datas"
)
