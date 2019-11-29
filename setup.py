import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alphab",
    version="0.1",
    author="Julia Jakubczak",
    author_email="jjakubczak@wikia-inc.com",
    description="Python library for rendering charts and computing statistics for A/B testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wikia/AlphaB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
