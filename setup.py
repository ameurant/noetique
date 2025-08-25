from setuptools import find_packages
from setuptools import setup

setup(
    name="noetique",
    version="6.1",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    install_requires=[
        "Products.CMFPlone",
        "z3c.jbot",
    ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
        """,
)
