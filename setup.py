#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
from glob import iglob
from os.path import basename, splitext

from setuptools import find_packages, setup  # type: ignore

long_description: str
with open("README.markdown", encoding='utf-8') as f:
    long_description = f.read()
    print(long_description)

setup(
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    author="",
    author_email='',
    description="",
    include_package_data=True,
    keywords="",
    long_description_content_type='text/markdown',
    long_description=long_description,
    name="ai_project",
    package_dir={"": "src"},
    packages=find_packages("src"),
    py_modules=[splitext(basename(path))[0] for path in iglob("src/*.py")],
    python_requires=">=3.6",
    url="",
    version="0.0.0",
    zip_safe=False,
)
