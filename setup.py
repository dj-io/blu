from setuptools import setup, find_packages

setup(
    name="apollo",
    version="0.3.0",
    description="A CLI tool for automating developer workflows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Stratum Labs",
    author_email="hq@stratumlabs.ai",
    url="https://github.com/dj-io/apollo",
    packages=find_packages(where="apollo"),
    install_requires=[
        "questionary",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "apollo=apollo.main:apollo",  # Maps the `apollo` command to the `apollo()` group function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
)