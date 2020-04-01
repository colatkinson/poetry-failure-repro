import setuptools

setuptools.setup(
    name="example-pkg",
    version="0.0.1",
    author="Colin Atkinson",
    author_email="colin@atakama.com",
    description="A small example package",
    packages=["example_pkg", "another_pkg"],
    python_requires='>=3.6',
)
