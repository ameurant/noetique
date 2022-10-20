# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = "6.0.1"

setup(
    name="noetique",
    version=version,
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    author="Sébastien Verbois",
    author_email="sebastien.verbois@gmail.com",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Products.CMFPlone",
        "z3c.jbot",
    ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
        """,
)
