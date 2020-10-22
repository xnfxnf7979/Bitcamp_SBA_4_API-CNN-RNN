import setuptools
# root directory 에서 pip install .
with open("Readme.py","r",encoding='utf-8') as fh:
    long_description  = fh.read()

setuptools.setup(
    name='com_sba_api',
    version='1.0',
    description='Python Distribution Utilities',
    long_description=long_description,
    author='MCY',
    author_email='xnfxnf7979@daum.net',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)