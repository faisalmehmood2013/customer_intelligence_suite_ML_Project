"""
setup.py
----------
Yeh file project ko ek INSTALLABLE PYTHON PACKAGE banati hai
(taake "from customer_intelligence_suite.utils import ..." jaise
imports kaam karein, project ko kahin se bhi).

Standard setup.py (aap ke template jaisa hi):

    from setuptools import find_packages, setup

    setup(
        name="customer_intelligence_suite",
        version="0.0.1",
        author="Faisal",
        packages=find_packages(),
        install_requires=[],   # requirements.txt se separately install karenge
    )

Phir terminal mein: pip install -e .
"""
