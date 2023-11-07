# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="pioreactor-air-bubbler",
    version="0.3.3",
    license="MIT",
    description="Add an air bubbler to your Pioreactor as a background job",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="hello@pioreactor.com",
    author="Pioreactor",
    url="https://github.com/Pioreactor/pioreactor-air-bubbler",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pioreactor.plugins": "pioreactor_air_bubbler = pioreactor_air_bubbler"
    },
)
