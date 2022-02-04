import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packagename",
    version="0.1.5",
    author="Atharva Kulkarni",
    author_email="sampleemail@gmail.com",
    description="A Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/packagename",
    packages=setuptools.find_packages(),
    install_requires  = ['Click','requests',...], # List all your dependencies inside the list
    license = 'MIT'
)