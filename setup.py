# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

packages = ["duo_cli"]

install_requires = ["pyotp>=2.3.0", "pyqrcode>=1.2.1", "requests>=2.22.0"]

entry_points = {
    "console_scripts": [
        "duo_activate = duo_cli.duo_activate:main",
        "duo_export = duo_cli.duo_export:main",
        "duo_gen = duo_cli.duo_gen:main",
    ]
}

setup_kwargs = {
    "name": "duo-cli",
    "version": "1.0.0",
    "description": "Duo CLI HOTP Password Generator",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/macmisu/duo-cli",
    "packages": packages,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.6,<4.0",
}

setup(**setup_kwargs)
